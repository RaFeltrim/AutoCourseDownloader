
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
  - Utiliza `ThreadPoolExecutor` para realizar downloads e extrações simultaneamente, otimizando o desempenho.

- **Log Detalhado:**
  - Registra todas as etapas do processo e possíveis erros no arquivo `download_logs.log`.

---

## 🚀 Como Usar

### 1. Clone o Repositório
```bash
git clone https://github.com/RaFeltrim/AutoCourseDownloader.git
cd AutoCourseDownloader
```

### 2. Instale as Dependências
Certifique-se de ter o Python instalado (>=3.8). Em seguida, instale os pacotes necessários:
```bash
pip install -r requirements.txt
```

### 3. Configure o CSV
Abra o arquivo `links.csv` e insira os links e nomes dos arquivos no seguinte formato:

```csv
Nome,Link
Curso de Python Básico,https://drive.google.com/file/d/EXEMPLO2/view?usp=sharing
```

### 4. Execute o Script
Inicie o processo de download e extração:
```bash
python main2.py
```

### 5. Verifique os Resultados
- Os arquivos baixados serão extraídos automaticamente para a pasta `downloads`.
- Consulte o log em `download_logs.log` para verificar o status de cada download e extração.

---

## 📁 Estrutura do Projeto

```
AutoCourseDownloader/
│
├── links.csv             # Lista de links e nomes dos arquivos
├── main2.py              # Script principal
├── requirements.txt      # Dependências do Python
├── download_logs.log     # Logs de execução
└── README.md             # Documentação do projeto
```

---

## 🌟 Tecnologias Utilizadas

- **Python**: Linguagem de programação para automação e manipulação de arquivos.
- **gdown**: Para realizar downloads de arquivos do Google Drive.
- **patoolib**: Utilizada para extrair arquivos compactados no formato `.rar`.
- **pandas**: Para manipulação de dados em CSV.
- **ThreadPoolExecutor**: Para execução paralela de downloads e extrações.
- **logging**: Para gerenciar logs detalhados das operações.

---

## 📚 Aprendizados

Este projeto permitiu o desenvolvimento das seguintes habilidades:
- Automação de processos repetitivos usando Python.
- Gerenciamento eficiente de dependências e estruturação de projetos.
- Implementação de execução paralela com `ThreadPoolExecutor` para otimização de desempenho.
- Manipulação de arquivos e integração com bibliotecas externas.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar **pull requests**. Todo tipo de ajuda é apreciado.

---

## 📧 Contato

Criado por [Rafael Feltrim](https://github.com/RaFeltrim). Para dúvidas ou sugestões, entre em contato pelo e-mail: [rafeltrim@gmail.com](mailto:rafeltrim@gmail.com)
