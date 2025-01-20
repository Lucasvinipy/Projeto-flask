from flask import Blueprint , render_template
from database.cliente import CLIENTES 

cliente_route = Blueprint('cliente',__name__)

"""""
     - /cliente/ (GET) - listar os clientes 
     - /cliente/ (POST) - inserir o cliente no servidor
     - /cliente/new (GET) - renderizar o formulario para criar um cliente
     - /cliente/<id> (GET) - obter os dados do cliente 
     - /cliente/<id>/EDIT (GET) - renderizar formulario para editar cliente 
     - /cliente/<id>/update (PUT) - atualizar os dados do cliente 
     - /cliente/<id>/delete (DELETE) - deleta o registro do usuario 
"""""

@cliente_route.route('/')
def lista_cliente():
   return render_template('lista_clientes.html', clientes=CLIENTES)


@cliente_route.route('/', methods = ['POST'])
def inserir_cliente():
   pass


@cliente_route.route('/new')    
def Form_cliente():
   return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def Detalhe_cliente(cliente_id):
   return render_template('Detalhe_cliente.html')


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
   return render_template('form_edit_cliente.html')


@cliente_route.route('/<int:cliente_id>/update', methods = ['PUT'])
def update_cliente(cliente_id):
   pass 

@cliente_route.route('/<int:cliente_id>/delete', methods = ['DELETE'])
def deletar_cliente(cliente_id):
   pass 