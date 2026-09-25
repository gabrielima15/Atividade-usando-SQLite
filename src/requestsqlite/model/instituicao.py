class Instituicao():

    def __init__(
        self,
        id,
        no_entidade,
        co_entidade,
        no_uf,
        sg_uf,
        co_uf,
        no_municipio,
        co_municipio,
        nu_ano_censo,
        qt_mat_bas=0,
        qt_mat_inf=0,
        qt_mat_fund=0,
        qt_mat_med=0,
        qt_mat_prof=0,
        qt_mat_eja=0,
        qt_mat_esp=0
    ):
        self.id = id
        self.no_entidade = no_entidade
        self.co_entidade = co_entidade
        self.no_uf = no_uf
        self.sg_uf = sg_uf
        self.co_uf = co_uf
        self.no_municipio = no_municipio
        self.co_municipio = co_municipio
        self.nu_ano_censo = nu_ano_censo
        self.qt_mat_bas = qt_mat_bas
        self.qt_mat_inf = qt_mat_inf
        self.qt_mat_fund = qt_mat_fund
        self.qt_mat_med = qt_mat_med
        self.qt_mat_prof = qt_mat_prof
        self.qt_mat_eja = qt_mat_eja
        self.qt_mat_esp = qt_mat_esp

    def toDict(self):
        return {
            "id": self.id,
            "no_entidade": self.no_entidade,
            "co_entidade": self.co_entidade,
            "no_uf": self.no_uf,
            "sg_uf": self.sg_uf,
            "co_uf": self.co_uf,
            "no_municipio": self.no_municipio,
            "co_municipio": self.co_municipio,
            "nu_ano_censo": self.nu_ano_censo,
            "qt_mat_bas": self.qt_mat_bas,
            "qt_mat_inf": self.qt_mat_inf,
            "qt_mat_fund": self.qt_mat_fund,
            "qt_mat_med": self.qt_mat_med,
            "qt_mat_prof": self.qt_mat_prof,
            "qt_mat_eja": self.qt_mat_eja,
            "qt_mat_esp": self.qt_mat_esp
        }