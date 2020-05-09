# reviews

### Installation Steps

#### System Setup
`brew install dbmate`

`brew install pyenv`

`pyenv install 3.8.2`

`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`

`brew install postgresql` (version 12.2)

`createuser -s postgres`

`createdb -U postgres reviews`

`createdb -U postgres reviews_test`

`psql -U postgres`

#### Project Setup

##### First time
`pyenv which python| pbcopy`

`poetry env use <python path>`


##### Install dependecnies
`poetry install`

Note: Psycopg2 has known issues on Mac 
env LDFLAGS="-I/usr/local/opt/openssl/include -L/usr/local/opt/openssl/lib" poetry add psycopg2=^2.8.5
