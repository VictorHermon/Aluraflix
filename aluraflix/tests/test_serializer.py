from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):

    def setUp(self) -> None:
        self.programa = Programa(
            titulo='Procurando ninguém em latim',
            data_lancamento='2003-07-04',
            tipo='F',
            likes=2340,
            dislikes=40
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verificar_campos_serializados(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEquals(set(data.keys()), {'titulo', 'data_lancamento', 'tipo', 'likes'})

    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica o conteudo dos campos serializados"""
        data = self.serializer.data
        self.assertEquals(data['titulo'], self.programa.titulo)
        self.assertEquals(data['tipo'], self.programa.tipo)
        self.assertEquals(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEquals(data['likes'], self.programa.likes)
