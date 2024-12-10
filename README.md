# AutoCourseDownloader

Um projeto Python para automatizar o download e extração de arquivos de cursos hospedados no Google Drive, utilizando processamento paralelo para maior eficiência. Este projeto é ideal para gerenciar grandes volumes de downloads de forma automatizada.

---

## 🛠️ Funcionalidades

- **Download Automático:**
  - Realiza o download de arquivos do Google Drive a partir de links especificados em um arquivo CSV.
  - Verifica se o arquivo já foi baixado, evitando duplicações.

- **Extração de Arquivos:**
  - Extrai arquivos compactados no formato `.rar` para diretórios específicos.
  - Realiza verificações para garantir a integridade dos arquivos extraídos.

- **Execução Paralela:**
  - Utiliza `ThreadPoolExecutor` para realizar downloads e extrações simultaneamente.

- **Log Detalhado:**
  - Registra todas as etapas do processo e possíveis erros no arquivo `download_logs.log`.

---

## 🚀 Como Usar

### 1. Clone o Repositório
```bash
git clone https://github.com/seuusuario/AutoCourseDownloader.git
cd AutoCourseDownloader
```

### 2. Instale as Dependências
Certifique-se de ter o Python instalado (>=3.8). Em seguida, instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

### 3. Configure o CSV
- Abra o arquivo `links.csv` e insira os links e nomes dos arquivos no seguinte formato:
  ```csv
  Link,Nome
  https://drive.google.com/file/d/EXEMPLO/view,Curso_1
  https://drive.google.com/file/d/EXEMPLO2/view,Curso_2
  ```

### 4. Execute o Script
Inicie o processo de download e extração:
```bash
python main2.py
```

### 5. Verifique os Resultados
- Os arquivos baixados serão extraídos para a pasta `downloads`.
- Consulte o log em `download_logs.log` para verificar detalhes do processo.

---

## 📁 Estrutura do Projeto

```
AutoCourseDownloader/
│
├── links.csv             # Links e nomes dos arquivos
├── main2.py              # Script principal
├── requirements.txt      # Dependências do Python
├── download_logs.log     # Logs de execução
└── README.md             # Documentação do projeto
```

---

## 🌟 Tecnologias Utilizadas

- **Python** (Automatização e Manipulação de Arquivos)
- **gdown** (Download de Arquivos do Google Drive)
- **patoolib** (Extração de Arquivos `.rar`)
- **pandas** (Manipulação do CSV)
- **ThreadPoolExecutor** (Execução Paralela)
- **logging** (Gerenciamento de Logs)

---

## 📚 Aprendizados

Este projeto demonstra habilidades em:
- Automatação de processos repetitivos com Python.
- Gerenciamento de dependências e organização de projetos.
- Uso de ferramentas como `ThreadPoolExecutor` para execução eficiente.
- Manipulação de arquivos e integração de bibliotecas externas.

---

## 🤝 Contribuições

Sinta-se à vontade para abrir issues e enviar pull requests. Todo tipo de contribuição é bem-vindo!

---

## 📧 Contato

Criado por [Seu Nome](https://github.com/RaFeltrim). Para dúvidas, entre em contato pelo e-mail: rafeltrim@gmail.com
