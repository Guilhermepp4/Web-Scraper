# Web Scraper

## 📌 Descrição

Este projeto consiste num script de web scraping desenvolvido para extrair imagens e nomes de produtos de uma página de catálogo online de artigos em latão.

O objetivo principal foi recolher imagens de produtos previamente autorizados pelo cliente (drogaria local) e processá-las para utilização consistente num catálogo digital.

Após a extração, as imagens são automaticamente descarregadas, redimensionadas para um formato uniforme e guardadas localmente com nomes normalizados.

---

## 🏢 Contexto do Projeto

Este trabalho foi realizado para uma drogaria local que solicitou a recolha de imagens de produtos de um fornecedor online previamente autorizado.

O objetivo foi facilitar a criação de um catálogo web organizado e padronizado.

---

## 🌐 Fonte dos Dados

Os dados foram extraídos do seguinte website:

* https://casamariomachado.pt/284-artigos-de-latao-para-pichelaria

---

## ⚙️ Funcionalidades

* Extração automática de dados HTML com BeautifulSoup
* Navegação por múltiplas páginas do catálogo
* Recolha de:

  * Nome do produto
  * URL da imagem
  * Página em que se encontra o produto
* Exportação de dados estruturados em JSON
* Download automático das imagens
* Redimensionamento para **300x300 pixels**
* Normalização de nomes de ficheiros

---

## 🧰 Tecnologias Utilizadas

* Python 3
* requests
* BeautifulSoup4
* Pillow (PIL)
* json
* os
* io (BytesIO)

---

## 📁 Estrutura do Projeto

```
.
├── data/
│   └── images.json        # metadata dos produtos extraídos
├── images/                # imagens finais processadas (300x300)
├── scraper.py            # script principal de scraping
└── README.md
```

---

## 🚀 Como executar

### 1. Instalar dependências

```bash
pip install requests beautifulsoup4 pillow
```

---

### 2. Executar o scraper

```bash
python scraper.py
```

---

## 🔄 Processo de funcionamento

1. O script percorre todas as páginas do catálogo
2. Extrai nome e imagem de cada produto bem como a página em que se encontra
3. Guarda os dados num ficheiro JSON
4. Faz download das imagens
5. Converte e redimensiona para 300x300 px
6. Guarda as imagens localmente com nomes normalizados

---

## ⚠️ Notas importantes

* O scraping foi realizado apenas em páginas com autorização do cliente.
* Algumas imagens podem ser ignoradas automaticamente caso sejam placeholders ou inválidas.
* O sistema assume que as imagens são acessíveis publicamente via URL.

---

## 📦 Resultado final

* Dataset estruturado de produtos
* Imagens padronizadas para catálogo
* Base pronta para integração em website

---

## 👨‍💻 Autor

Desenvolvido por Guilherme Pinho (projeto freelance)

---

## 📜 Licença

Projeto sob autorização do cliente.
