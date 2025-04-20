from config.db.db_config import pegar_conexao
from config.logs.log_config import registrar_log

def pegar():
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM area')
        areas = cursor.fetchall()
        return areas
    except Exception as e:
        message_error = f"Erro ao buscar áreas: {str(e)}"
        registrar_log("area_repositorio", "pegar", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def pegar_por_id(id):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM area WHERE id = :1', [id])
        area = cursor.fetchone()
        return area
    except Exception as e:
        message_error = f"Erro ao buscar área por ID: {str(e)}"
        registrar_log("area_repositorio", "pegar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def criar(nome, localizacao, hectar):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        id_var = cursor.var(int)
        cursor.execute(
            'INSERT INTO area (nome, localizacao, hectar) VALUES (:1, :2, :3) RETURNING id INTO :4',
            [nome, localizacao, hectar, id_var]
        )
        conexao.commit()
        registrar_log("area_repositorio", "criar", "Sucesso", f"Área criada com sucesso - id: {str(id_var.getvalue()[0])}, nome: {str(nome)}, localização: {str(localizacao)}, hectares: {str(hectar)}")
        return id_var.getvalue()[0]
    except Exception as e:
        message_error = f"Erro ao criar área: {str(e)}"
        registrar_log("area_repositorio", "criar", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def atualizar_por_id(id, nome, localizacao, hectar):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            'UPDATE area SET nome = :1, localizacao = :2, hectar = :3 WHERE id = :4',
            [nome, localizacao, hectar, id]
        )
        conexao.commit()
        registrar_log("area_repositorio", "atualizar_por_id", "Sucesso", f"Área atualizada com sucesso - id: {str(id)}, nome: {str(nome)}, localização: {str(localizacao)}, hectares: {str(hectar)}")
        return cursor.rowcount > 0
    except Exception as e:
        message_error = f"Erro ao atualizar área: {str(e)}"
        registrar_log("area_repositorio", "atualizar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()

def deletar_por_id(id):
    try:
        conexao = pegar_conexao()
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM area WHERE id = :1', [id])
        conexao.commit()
        registrar_log("area_repositorio", "deletar_por_id", "Sucesso", f"Área deletada com sucesso - id: {str(id)}")
        return cursor.rowcount > 0
    except Exception as e:
        message_error = f"Erro ao deletar área: {str(e)}"
        registrar_log("area_repositorio", "deletar_por_id", "Erro", message_error)
        raise Exception(message_error)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conexao' in locals():
            conexao.close()