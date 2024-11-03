# ITA-IME Downloader

Script para salvar todas as aulas preparatórias do Colégio Ari de Sá para o concurso do ITA





## Instalação

Clone o repositório:
```bash
git clone https://github.com/OtaviOuu/ITA-IME-ArideS-Downloader
```

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar as dependências:

```bash
pip install -r requirements.txt
```

## Executando
Dentro do repositório clonado:

```bash
python src/main.py
```


## Resultado

No terminal você deve ver algo como:
```python
- INFO    - Vídeo encontrado: Aula 31                          - [link]
- WARNING - Sem vídeo: TC de APROFUNDAMENTO 11 - RESOLUÇÕES
- INFO    - Vídeo encontrado: Aula 16                          - Teoria do orbital molecular - [link]
- INFO    - Vídeo encontrado: Aula 30                          - Esfera Condutora            - [link]
- INFO    - Vídeo encontrado: Aula 30                          - Parábola de segurança       - [link]
- INFO    - Vídeo encontrado: Aula 32                          - Cap. 3 Top. 1G             - [link]
- INFO    - Vídeo encontrado: Aula 06                          - Comentários Simulado 2      - [link]
- INFO    - Vídeo encontrado: Aula 35                          - cap 3 top 2 a              - [link]
- INFO    - Vídeo encontrado: Aula 26                          - Resolução de Questões       - [link]
- INFO    - Vídeo encontrado: Aula 27                          - Resolução de Questões       - [link]
- INFO    - Vídeo encontrado: Aula 29                          - Revisão                    - [link]
- INFO    - Vídeo encontrado: Aula 20                          - Continuação Revisão         - [link]
- INFO    - Vídeo encontrado: Aula 45                          - Revisão IME                - [link]
- WARNING - Sem vídeo: Exercício Complementar Ondulatória - MHS - Cap 2, 3 e 4
- INFO    - Vídeo encontrado: Aula 20                          - Cálculo de Potencial Elétrico - [link]

...
```

Ao final, o script criará um arquivo json no formato:

```json
"[Módulo]": {
        "[Titulo da Aula]": "[Link da Aula]",
        "[Titulo da Aula]": "[Link da Aula]",
        "[Titulo da Aula]": "[Link da Aula]",
        "[Titulo da Aula]": "[Link da Aula]",
        "[Titulo da Aula]": "[Link da Aula]",
        "[Titulo da Aula]": "[Link da Aula]",
        "[Titulo da Aula]": "[Link da Aula]",
        "[Titulo da Aula]": "[Link da Aula]",
        "[Titulo da Aula]": "[Link da Aula]",
        "[Titulo da Aula]": "[Link da Aula]",
        "[Titulo da Aula]": "[Link da Aula]",
        "[Titulo da Aula]": "[Link da Aula]",
        ...
}
```
Exemplo:
```json
"2023 3o ITA/IME Matemática 1": {
        "Aula 01 - 13/01/2023 - 18:40 - Fatorial": "[link]",
        "Aula 02 - 20/01/2023 - 18:40 - Combinatória": "[link]",
        "Aula 03 - 27/01/2023 - 18:40 - Resolução de questões": "[link]",
        ...
        }

```
