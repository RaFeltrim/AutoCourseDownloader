import os
import gdown
import patoolib
import shutil
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Função para baixar o arquivo usando gdown
def download_file(link, nome):
    try:
        # Caminho do arquivo de saída
        output = os.path.join('D:/cursos', f'{nome}.rar')
        
        # Verificar se o arquivo já existe
        if os.path.exists(output):
            logging.info(f"O arquivo {output} já existe. Pulando download...")
            return None
        
        # Extrair o ID do arquivo do link do Google Drive
        file_id = link.split('/d/')[1].split('/')[0]
        url = f'https://drive.google.com/uc?id={file_id}&confirm=t'
        
        logging.info(f"Baixando {nome} de {url} para {output}...")

        # Usar gdown para baixar o arquivo
        gdown.download(url, output, quiet=False)
        
        logging.info(f"Download concluído: {output}")
        return output
    except Exception as e:
        logging.error(f"Erro ao baixar o arquivo {nome}: {e}")
        return None

# Função para extrair arquivos .rar
def extract_file(file_path):
    try:
        extraction_folder = file_path.replace('.rar', '')
        logging.info(f"Extraindo {file_path} para {extraction_folder}...")

        patoolib.extract_archive(file_path, outdir=extraction_folder)

        # Verificar tamanho do arquivo extraído
        extracted_size = sum(os.path.getsize(os.path.join(dirpath, filename)) 
                             for dirpath, _, filenames in os.walk(extraction_folder) 
                             for filename in filenames)
        
        logging.info(f"Tamanho do arquivo extraído: {extracted_size} bytes")

        # Verificar se o arquivo foi extraído corretamente (por exemplo, maior que 90 KB)
        if extracted_size > 90000:
            logging.info(f"Arquivo extraído com sucesso: {file_path}")
            # Apagar o arquivo .rar
            os.remove(file_path)
            logging.info(f"Arquivo .rar apagado: {file_path}")
        else:
            logging.error(f"Erro: Tamanho do arquivo extraído é muito pequeno: {extracted_size} bytes")

    except Exception as e:
        logging.error(f"Erro ao extrair o arquivo {file_path}: {e}")

# Função principal para gerenciar downloads e extrações
def main():
    # Carregar a planilha CSV com os links
    links = pd.read_csv('links.csv')

    total_links = len(links)
    logging.info(f"Número total de links no arquivo: {total_links}")

    # Fazer download e extração em lotes de 3 arquivos por vez
    for i in range(0, total_links, 3):
        with ThreadPoolExecutor() as executor:
            # Usar row[1]['Link'] e row[1]['Nome'] porque iterrows retorna um índice e uma série
            file_paths = list(executor.map(lambda row: download_file(row[1]['Link'], row[1]['Nome']), links.iloc[i:i + 3].iterrows()))

            # Extração dos arquivos baixados
            for file_path in file_paths:
                if file_path:
                    extract_file(file_path)

if __name__ == '__main__':
    main()
