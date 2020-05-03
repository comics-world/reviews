# reviews

### Installation Steps

#### System Setup
`brew install pyenv`
`pyenv install 3.8.2`
`curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python`

#### Project Setup

##### First time
`pyenv which python| pbcopy`
`poetry env use <python path>`

##### Install dependecnies
`poetry install`
