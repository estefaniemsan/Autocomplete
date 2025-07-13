Comentários sobre o Projeto de busca autocomplete
---------------------------------------------------------------------------------------
Este projeto foi o meu primeiro contato com algo realmente completo e complexo, confesso que aprendi muitas coisas e explorei ao máximo as ideias, criatividade e opções. 

Como meu primeiro contato com conexões de api, url's e conexão back+frontend precisei quebrar o projeto em partes para conseguir estruturar e organizar as ideias. Utilizei ajuda de literaturas disponíveis na web pra me auxiliar em testes e no uso do terminal com os comandos e configurações 

--------------------------------------------------------------------------------------------
Ideias Backend que foram abandonadas:

-- Gemini: De início tentei fazer uma versão de back end que cominicasse com o gemini para mockar uma base e pesquisar termos que ainda não existiam 
    Essa ideia n funcionou por conta de coneções via API, não funcionava para buscas fora do escopo pré definido na minha base json (Base fake)

-- Serchapi: Mudei a api com esperança que desse certo mas não funcionou, acredito que por falta de conhecimento e por motivos semelhantes ao anterior

-- Kaggle: Busquei bases de palavras mais frequentes, mas o escopo é muito limitado no portugês e não consiguiria fazer autocomplete de orações. Procurei por Arvores de sufixo também, mas não encontrei nada viáve.

-- Pytrends: Foi ai que tive a ideia de usar os assuntos mais falados como base de autocomplete, tentei conectar com essa biblioteca python, mas tive problemas de importação, logo a busca não retornava valor algum

--------------------------------------------------------------------------------------------------

Backend Atual: Flask (Python)

Seguindo pela mesma ideia, cheguei a terceira versão kkkkkk, atualmente conhecida como scrapping, onde literalmente pesquiso as sugestões em uma url google e coleto as orações obtidas. 

Utilizei o Flask, flask_cors, requests e algumas outras bibliotecas para me auxiliarem na conexão via api (confesso que ainde tenho muito que aprender nesse quesito)

Se tivesse mais tempo gostaria de explorar conexões via Mongodb, e ter usado o Graphql, infelizmente pela limitação de tempo (estagio + semana de provas), preferi focar na funcionalidade e acabei não conseguindo entender como funcionaria essa conexão, implentar e testar. 

------------------------------------------------------------------------------------------------
Frontend React

Aqui foi minha zona de conforto, fiz algo simples, mas que funcionasse sem muitos problemas, já tinha familiaridade com o react e com os comando do css o que acabou facilitando.

Gosto de brincar com as cores, frames e posicionamentos e fontes.
Ainda assim com alguns bugs que gostaria de resolver, e com certeza vou kkkkkk

Implementações futuras:
-- Gostaria de colocar um botão de pesquisa que redirecionasse para uma pagína correspondente 
-- adicionar funções de teclas (Enter, baixo, cima)
-- Adicionar histórico de pesquisas (em uma aba ou trocar o ícone quando for recente)
-- Realizar apenas o autocomplete (não exibir palavas que contenham o digitado)
-- Atalhos com teclas enter e setas para navegação



