from app.models.cep_model import buscar_cep

def get_cep_data(cep):
    if not cep or not cep.isdigit() or len(cep) != 8:
        return {'erro':'cep_invalido'}
    
    data = buscar_cep(cep)

    if not data:
        return {'erro': 'O CEP não foi encontrado ou a API está indisponível'}
    
    return{
        'logradouro':data.get('logradouro'),
        'bairro':data.get('bairro'),
        'cidade':data.get('cidade'),
        'estado':data.get('estado')
    }
