class load_txt:
    def __init__(self, name) -> None:
        self.name = name
        self.tab = self.load_txt_file()
    
    def load_txt_file(self) -> list:
        f = open(self.name)
        lines = f.readlines()
        n = len(lines[0].split())
        tab = [[] for _ in range(n)]
        for i in lines:
            l = i.split()
            for j, v in enumerate(l):
                tab[j].append(v)
        return tab
    
    def get_ele(self, e, col):
        ind_col = [i[0] for i in self.tab].index(col)
        if not ind_col: return ('sir t9wd colonne inexistante')
        ind = [i for i,v in enumerate(self.tab[ind_col]) if v==e]; l =[]
        if not ind: return ('sir t9wd element inexistant')
        for i in ind:
            l.append(self.get_row(i))
        return l
        
    
    def get_row(self, ind):
        return [i[ind] for i in self.tab]
        
txt = load_txt("C:/Users/HP/Desktop/vsCode/centrale/scolarite_app/t.txt")
print(txt.load_txt_file())
print(txt.get_row(2))
print(txt.get_ele("@", "mail"))