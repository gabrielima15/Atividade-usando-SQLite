from flask import Flask, request
from .database import get_connection
from .model.instituicao import Instituicao
from .model.usuario import Usuario
import sqlite3


app = Flask(__name__)


# FEITO.
@app.get('/instituicoes')
def listarInstituicoes():

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT
            id,
            no_entidade,
            co_entidade,
            no_uf,
            sg_uf,
            co_uf,
            no_municipio,
            co_municipio,
            nu_ano_censo,
            qt_mat_bas,
            qt_mat_inf,
            qt_mat_fund,
            qt_mat_med,
            qt_mat_prof,
            qt_mat_eja,
            qt_mat_esp
            FROM tb_instituicao_ensino where is_delete = false""")
        rows = cursor.fetchall()

        instituicoesAll = [
            Instituicao(*row).toDict()
            for row in rows
        ]

        return instituicoesAll, 200

    except sqlite3.Error as e:
        return {"error": str(e)}, 500

    finally:
        if conn is not None:
            conn.close()

#FEITO.
@app.get('/instituicoes/<int:id>')
def getInstituicaoById(id):
    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT
            id,
            no_entidade,
            co_entidade,
            no_uf,
            sg_uf,
            co_uf,
            no_municipio,
            co_municipio,
            nu_ano_censo,
            qt_mat_bas,
            qt_mat_inf,
            qt_mat_fund,
            qt_mat_med,
            qt_mat_prof,
            qt_mat_eja,
            qt_mat_esp
            FROM tb_instituicao_ensino WHERE id = ? AND is_delete = false
            """,
            (id,)
        )
        row = cursor.fetchone()

        if row:
            return {
                "instituicao": Instituicao(*row).toDict()
            }, 200

        return {
            "error": "Instituição não encontrada"
        }, 404

    except sqlite3.Error as e:
        return {
            "error": str(e)
        }, 500

    finally:
        if conn is not None:
            conn.close()


# FEITO.
@app.post('/instituicoes')
def criarInstituicao():

    data = request.get_json()

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO tb_instituicao_ensino (
                no_entidade,
                co_entidade,
                no_uf,
                sg_uf,
                co_uf,
                no_municipio,
                co_municipio,
                nu_ano_censo,
                qt_mat_bas,
                qt_mat_inf,
                qt_mat_fund,
                qt_mat_med,
                qt_mat_prof,
                qt_mat_eja,
                qt_mat_esp
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, tuple(data.values()))

        conn.commit()

        return {
            "message": "Instituição criada com sucesso",
        }, 201

    except sqlite3.Error as e:

        if conn is not None:
            conn.rollback()

        return {"error": str(e)}, 500

    finally:
        if conn is not None:
            conn.close()

# FEITO
@app.put('/instituicoes/<int:id>')
def putInstituicao(id):

    data = request.get_json()

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE tb_instituicao_ensino
            SET
                no_entidade = ?,
                co_entidade = ?,
                no_uf = ?,
                sg_uf = ?,
                co_uf = ?,
                no_municipio = ?,
                co_municipio = ?,
                nu_ano_censo = ?,
                qt_mat_bas = ?,
                qt_mat_inf = ?,
                qt_mat_fund = ?,
                qt_mat_med = ?,
                qt_mat_prof = ?,
                qt_mat_eja = ?,
                qt_mat_esp = ?
            WHERE id = ?
        """, (data["no_entidade"], data["co_entidade"],
              data["no_uf"], data["sg_uf"], data["co_uf"],
              data["no_municipio"], data["co_municipio"], data["nu_ano_censo"],
              data["qt_mat_bas"], data["qt_mat_inf"], data["qt_mat_fund"], 
              data["qt_mat_med"], data["qt_mat_prof"], data["qt_mat_eja"], 
              data["qt_mat_esp"], id))

        conn.commit()

        if cursor.rowcount == 0:
            return {
                "error": "Instituição não encontrada"
            }, 404

        return {
            "message": "Instituição atualizada com sucesso"
        }, 200

    except sqlite3.Error as e:

        if conn is not None:
            conn.rollback()

        return {
            "error": str(e)
        }, 500

    finally:
        if conn is not None:
            conn.close()
    
# FEITO.
@app.delete('/instituicoes/<int:id>')
def deletarInstituicao(id):

    conn = None

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE tb_instituicao_ensino SET is_delete = true WHERE id = ?",
            (id,)
        )

        conn.commit()

        if cursor.rowcount == 0:
            return {
                "error": "Instituição não encontrada"
            }, 404

        return {
            "message": "Instituição deletada com sucesso"
        }, 200

    except sqlite3.Error as e:

        if conn is not None:
            conn.rollback()

        return {
            "error": str(e)
        }, 500

    finally:
        if conn is not None:
            conn.close()
            
# ---------------------------------------------------------------------

# FEITO.
@app.get("/usuarios")
def getUsuarios():
    try:
        conect = get_connection()
        cursor = conect.cursor()
        cursor.execute("SELECT id, nome, email, senha FROM tb_usuario where is_delete = false")
        rows = cursor.fetchall()
        usuariosAll = [Usuario(*row).toDict() for row in rows]
        return {"usuarios": usuariosAll}
    except sqlite3.Error as e:
        return {"error": str(e)}, 500
    finally:
        conect.close()

# FEITO.
@app.post("/usuarios")
def postUsuario():
    conect = get_connection()
    cursor = conect.cursor()
    data = request.get_json()
    try:
        cursor.execute("""
            INSERT INTO tb_usuario (nome, email, senha)
            VALUES (?, ?, ?)
        """, (data["nome"], data["email"], data["senha"]))
        conect.commit()
        return {"message": "Usuário criado com sucesso"}, 201
    except sqlite3.Error as e:
        conect.rollback()
        return {"error na execução": str(e)}, 500
    finally:
        conect.close()

# FEITO.
@app.get("/usuarios/<int:id>")
def getUsuarioById(id):
    conect = get_connection()
    cursor = conect.cursor()
    try:
        cursor.execute("""
                    SELECT id, nome, email, senha
                    FROM tb_usuario WHERE id = ? AND is_delete = false
                    """, (id,))
        row = cursor.fetchone()
        if row:
            return {"usuario": Usuario(*row).toDict()}, 200
        else:
            return {"error": "Usuário não encontrado"}, 404
    except sqlite3.Error as e:
        return {"error na execução": str(e)}, 500
    finally:
        conect.close()

# FEITO.
@app.put("/usuarios/<int:id>")
def putUsuario(id):
    conect = get_connection()
    cursor = conect.cursor()
    data = request.get_json()
    try:
        
        cursor.execute("""
            UPDATE tb_usuario
            SET nome = ?, email = ?, senha = ?
            WHERE id = ?
        """, (data["nome"], data["email"], data["senha"], id))
        conect.commit()
        
        return {"message": "Usuário atualizado com sucesso"}, 200
    
    except sqlite3.Error as e:
        conect.rollback()
        return {"error": str(e)}, 500
    finally:
        conect.close()

# FEITO.
@app.delete("/usuarios/<int:id>")
def deleteUsuario(id):
    conect = get_connection()
    cursor = conect.cursor()
    try:
        cursor.execute("UPDATE tb_usuario SET is_delete = true WHERE id = ?", (id,))
        conect.commit()
        return {"message": "Usuário deletado com sucesso"}, 200
    except sqlite3.Error as e:
        conect.rollback()
        return {"error": str(e)}, 500
    finally:
        conect.close()


if __name__ == "__main__":
    app.run(debug=True)