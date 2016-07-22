# -*- coding : utf-8 -*-

import unittest
from modelos import Mensagem, Data, Json


class TestData(unittest.TestCase):

	def setUp(self):
		self.data = Data()

	def test_data_criada_deve_retornar_data_atual(self):
		from datetime import date
		self.assertEqual(date.today(),self.data.nativo())

	def test_data_deve_retornar_data_formatada_legivel(self):
		from datetime import date
		data_atual_formatada = date.today().strftime("%d/%m/%Y")

		self.assertEqual(data_atual_formatada,self.data.formatado())

class TestMensagem(unittest.TestCase):

	def setUp(self):
		self.mensagem = Mensagem("First Message","Content of message")

	def test_mensagem_deve_retornar_data_atual_quando_for_criada(self):
		from datetime import date

		data_atual = date.today()

		self.assertEqual(data_atual,self.mensagem.data.nativo())

	def test_mensagem_codificada_em_json_deve_retornar_formato_para_json(self):
		codificada = self.mensagem.to_dict()

		self.assertEqual(dict,type(codificada))
		
class TestJson(unittest.TestCase):

	def setUp(self):
		self.mensagem = Mensagem("First Message","Content message")
		self.json = Json("diario.json")

	def test_deve_carregar_de_um_arquivo_json_determinado_e_retornar_tipos_validos(self):
		tipos = [list,dict,str]

		conteudo_arquivo = self.json.carregar()

		self.assertIn(type(conteudo_arquivo),tipos)

	def test_deve_carregar_objeto_de_arquivo_e_ser_possivel_manipular(self):
		conteudo_arquivo = self.json.carregar()

		self.assertEqual(conteudo_arquivo[0]["titulo"],"First Message")
	
	def test_deve_poder_escrever_objetos_no_arquivo_json(self):
		import os

		tamanho_anterior = os.stat(self.json.arquivo).st_size

		self.json.gravar(self.mensagem.to_dict())
		
		tamanho_atual = os.stat(self.json.arquivo).st_size

		self.assertNotEqual(tamanho_anterior,tamanho_atual)


if __name__ == "__main__":
	unittest.main()
