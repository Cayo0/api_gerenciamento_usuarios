# Minha API com Django Rest Framework

Esta é uma API construída com Django Rest Framework (DRF) que fornece operações CRUD em um modelo de usuário personalizado. A autenticação JWT é necessária para acessar as views protegidas.

## Configuração do Ambiente

1. Clone este repositório:
   ```bash
   git clone https://github.com/Cayo0/api_gerenciamento_usuarios.git
   cd api_gerenciamento
   
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências:
pip install -r requirements.txt

4. Configure as variáveis de ambiente:
Crie um arquivo .env na raiz do projeto e defina as variáveis necessárias.Exemplo do .env:
SECRET_KEY=sua_chave_secreta
DEBUG=True

5. Aplique as migrações do banco de dados:
python manage.py migrate

6. Execute o servidor de desenvolvimento:
python manage.py runserver

Autenticação JWT:
Esta API usa autenticação JWT. Certifique-se de incluir um token JWT válido no cabeçalho Authorization ao fazer solicitações para views protegidas.

Endpoints:
Autenticação:
POST /api/token/: Obtém um token de acesso usando as credenciais do usuário.
POST /api/token/refresh/: Atualiza um token de acesso expirado.
POST /api/token/verify/: Verifica a validade de um token.

Esquema da API:
GET /api/schema/: Retorna o esquema da API no formato OpenAPI.
GET /api/schema/swagger-ui/: Exibe a documentação Swagger da API.

Autenticação de Token Clássica (authtoken):
POST /api-token-auth/: Obtém um token de acesso usando as credenciais do usuário (para autenticação baseada em token tradicional).

Recursos Personalizados (UsuariosViewSet):
GET /usuarios/: Lista todos os usuários.
GET /usuarios/{id}/: Detalhes de um usuário específico.
POST /usuarios/: Cria um novo usuário.
PUT /usuarios/{id}/: Atualiza um usuário existente.
DELETE /usuarios/{id}/: Exclui um usuário existente.
