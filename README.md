# 📂 Gerenciador de Arquivos `.txt` em Python

Este é um projeto simples em Python desenvolvido para gerenciar arquivos de texto (`.txt`) via terminal. O programa permite criar, listar, editar e excluir arquivos no diretório de execução.

---

## 🛠️ Estrutura e Explicação das Funções

O projeto é dividido em **3 módulos** para organizar a lógica do programa, a navegação de menus e a manipulação direta do sistema de arquivos.

---

### 📄 `arquivos.py`
Contém as funções responsáveis por interagir diretamente com os arquivos no disco.

* **`cria_arquivo()`**
  * **O que faz:** Solicita ao usuário o nome do arquivo, adiciona automaticamente a extensão `.txt` e cria um arquivo vazio no diretório atual.

* **`deleta_arquivo()`**
  * **O que faz:** Solicita o nome do arquivo que o usuário deseja excluir, adiciona a extensão `.txt`, verifica se ele existe na pasta e o remove do sistema usando `os.remove()`.

* **`edita_arquivo()`**
  * **O que faz:** Solicita o nome do arquivo `.txt` que o usuário quer alterar e insere o novo conteúdo digitado, sobrescrevendo o texto anterior.

---

### 📄 `menus.py`
Módulo responsável pelos submenus de navegação do sistema.

* **`mini_menu_edtArquivo()`**
  * **Significado do Nome:** **mini menu edita/editor Arquivo**.
  * **O que faz:** É um mini menu exclusivo acionado a partir da opção de edição do menu principal. Ele lista todos os arquivos `.txt` existentes e oferece um fluxo mais dinâmico para o usuário escolher entre:
    1. **Editar um arquivo existente** (chamando a função `edita_arquivo()`).
    2. **Criar um novo arquivo** para ser editado em seguida (chamando a função `cria_arquivo()`).
    3. **Voltar** ao menu principal.

---

### 📄 `main.py`
Arquivo principal de execução que contém o loop da aplicação (`while True`) e o menu principal com 5 opções:

1. **Criar arquivo:** Executa `cria_arquivo()`.
2. **Editar arquivo:** Abre o submenu `mini_menu_edtArquivo()`.
3. **Excluir arquivo:** Executa `deleta_arquivo()`.
4. **Mostrar arquivos:** Varre o diretório e exibe apenas os arquivos `.txt` juntamente com seus respectivos tamanhos em bytes (`os.path.getsize()`).
5. **Sair:** Finaliza a execução do programa.

---

## 🌲 Arquitetura e Dinâmica de Interação (Tree Mapa)

Abaixo está o mapa de dependências e de chamadas entre os módulos do sistema:

[ main.py ] (Ponto de Entrada)
   │
   ├── Opção 1 ──> cria_arquivo() ────────────> [ arquivos.py ]
   │
   ├── Opção 2 ──> mini_menu_edtArquivo() ────> [ menus.py ]
   │                   │
   │                   ├── Opção 1 ──> edita_arquivo() ──> [ arquivos.py ]
   │                   ├── Opção 2 ──> cria_arquivo()  ──> [ arquivos.py ]
   │                   └── Opção 3 ──> return ───────────> (Retorna ao main.py)
   │
   ├── Opção 3 ──> deleta_arquivo() ──────────> [ arquivos.py ]
   │
   ├── Opção 4 ──> Lista arquivos .txt usando `os.listdir()`
   │
   └── Opção 5 ──> Encerra o programa (`break`)
   
