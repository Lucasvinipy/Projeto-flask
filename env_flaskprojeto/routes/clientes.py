from flask import Blueprint , render_template , request
from database.models.cliente import Cliente

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

   clientes = Cliente.select()
   return render_template('lista_clientes.html', clientes=clientes)


@cliente_route.route('/', methods = ['POST'])
def inserir_cliente():  

   data = request.json

   novo_usuario = Cliente.create(
      nome = data['nome'],
      email = data['email'],     
   )

   return render_template('item_cliente.html', cliente = novo_usuario)

@cliente_route.route('/new')    
def Form_cliente():
   return render_template('form_cliente.html')


@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):

   cliente = Cliente.get_by_id(cliente_id)
   return render_template('detalhe_cliente.html', cliente = cliente)


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):

   cliente = Cliente.get_by_id(cliente_id)   
   return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods = ['PUT'])
def atualizar_cliente(cliente_id):

   

   data = request.json

   cliente_editado = Cliente.get_by_id(cliente_id)
   cliente_editado.nome = data['nome']
   cliente_editado.email = data['email']
   cliente_editado.save()

   return render_template('item_cliente.html',cliente= cliente_editado) 

@cliente_route.route('/<int:cliente_id>/delete', methods = ['DELETE'])
def deletar_cliente(cliente_id):
   cliente = Cliente.get_by_id(cliente_id)
   cliente.delete_instance()

   return{'deleted' : 'ok '}