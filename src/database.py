from csv import reader, writer, QUOTE_NONNUMERIC

class Database:
    """Classe pour la base des données stockés en format CSV"""

    DB_PATH: str = "data"
    TYPES: list[str] = ["int", "float", "varchar", "date", "time", "datetime"]
    CAST: list = [lambda x : int(x), lambda x : float(x), lambda x : x, lambda x : x, lambda x : x, lambda x : x]
    
    def __init__(self, name: str = "", filename: str = "") -> None:
        
        self.__name: str = name
        self.__filename: str = filename
        self.__content: dict[list] = dict()
        self.__header: list[str] = []
        self.__coltypes: list[int] = []
        self.__rows: list[list] = []

        with open(Database.DB_PATH + "\\" + filename, newline = "", mode = "r") as file:
            self.__rows = list(reader(file))
            self.__header = self.__rows[0]
            self.__coltypes = Database.__get_coltypes(self.__rows)
            self.__rows = Database.__cast_rows(self.__coltypes, self.__rows)
            self.__content = Database.__to_cols(self.__header, self.__rows)
    
    @staticmethod
    def __to_cols(header: list[str], rows: list[list]) -> dict[str, list]:
        result: dict = dict()
        for h in header:
            result.update({h: []})
        for row in rows[1:]:
            for i, h in enumerate(header):
                result[h].append(row[i])
        return result
    
    @staticmethod
    def __update_cols(content: dict[str, list] = dict(), row: list = []) -> dict[str, list]:
        header: list[str] = content.keys()
        result: dict[str, list] = {k: v for k, v in content.items()}
        for i, h in enumerate(header):
            result[h].append(row[i])
        return result
    
    @staticmethod
    def __cast_rows(coltypes: list[int], rows: list[int]) -> list[list]:
        result: list[list] = [rows[0]]
        for row in rows[1:]:
            l = []
            for i, x in enumerate(row):
                l.append(Database.CAST[coltypes[i]](x))
            result.append(l)
        return result
    
    @staticmethod
    def __get_coltypes(rows: list[list]) -> list[int]:
        coltypes: list[int] = []
        if len(rows) > 1:
            for x in rows[1]:
                coltypes.append(Database.__check(x))
        return coltypes
    
    @staticmethod
    def __duplicates(arr: list = []) -> list:
        result: list = []
        for x in arr:
            if not x in result:
                result.append(x)
        return result
    
    @staticmethod
    def __check(x = None) -> int:
        i: int = -1
        if x:
            i = 2
            try:
                x = int(x)
                i = 0
            except:
                pass
            
            if i > 0:
                try:
                    x = float(x)
                    i = 1
                except:
                    pass
        return i
    
    def select(self, *columns) -> dict[str, list]:
        result: dict = dict()
        for col in columns:
            if col in self.__header:
                result.update({col: self.__content[col]})
        return result
    
    def select_condition(self, **cond) -> dict[str, list]:
        rows: list[list] = [self.__header]
        for col, func in cond.items():
            if col in self.__header:
                idx = self.__header.index(col)
                for row in self.__rows[1:]:
                    if func(row[idx]):
                        rows.append(row)
        rows = Database.__duplicates(rows)
        return Database.__to_cols(self.__header, rows)
    
    def insert(self, row: list = []) -> None:
        if len(row) == len(self.__header) and Database.__get_coltypes([self.__header, row]) == self.__coltypes and not row[0] in [r[0] for r in self.__rows]:  
            with open(Database.DB_PATH + "\\" + self.__filename, newline = "", mode = "a") as file:
                self.__rows.append(row)
                self.__content = Database.__update_cols(self.__content, row)

                w = writer(file, delimiter = ",", quotechar = "\"", quoting = QUOTE_NONNUMERIC)
                w.writerow(row)
    

    def update(self) -> None:
        pass

    def contains(self, **cond) -> None:
        return len(self.select_condition(**cond)) > 0
                
    
    # Getters/Setters
                
    def get_content(self) -> dict[str, list]:
        return self.__content
    
    def get_name(self) -> str:
        return self.__name
    
    def get_filename(self) -> str:
        return self.__filename