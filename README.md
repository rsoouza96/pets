# Kenzie Pet


## Descrição

 Esse foi meu primeiro projeto em Django, feito pra aprender o básico sobre views, models e serializers.

## Instação

A instalação é simples, basta criar um ambiente virtual, instalar as dependencias que estão no requirements.txt. Para fazer isso basta rodar os comando:
1. python -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt


## Rotas

```
| Método | Rota  | Descrição  |

| :---:   | :-: | :-: |

| GET | /api/animals/ | Mostra todos os animais |

| GET | /api/animals/<int: animal_id> | Mostra um animal específico |

| POST | /api/animals/ | Cadastra um animal |


| DELETE | /api/animals/<int: animal_id> | Deleta um animal específico |
```

## Exemplo de requisição POST:
```
{                                               
"name": "Bidu",                                 
    "age": 1,                                   
    "weight": 30,                               
    "sex": "macho",                             
"group": {                                      
    "name": "cao",                              
    "scientific_name": "canis familiaris"       
    },                                          
"characteristic_set": [                         
    {                                           
    "characteristic": "peludo"                  
    },                                          
    {                                           
    "characteristic": "medio porte"             
    }                                           
]                                               
}                                               
```

## Exemplo de resposta:
```
200 Created
{
"id": 1,
"name": "Bidu",
"age": 1.0,
"weight": 30.0,
"sex": "macho",
"characteristic_set": [
    {
    "id": 1,
    "characteristic": "peludo"
    },
    {
    "id": 2,
    "characteristic": "medio porte"
    }
],
"group": {
    "id": 1,
    "name": "cao",
    "scientific_name": "canis familiaris"
}
}
```

