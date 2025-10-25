# 🧬 GENIAL — Genetic and Evolutionary Nature-Inspired Algorithms

![GitHub repo size](https://img.shields.io/github/repo-size/iuricode/README-template?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/iuricode/README-template?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/iuricode/README-template?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/iuricode/README-template?style=for-the-badge)
![Bitbucket open pull requests](https://img.shields.io/bitbucket/pr-raw/iuricode/README-template?style=for-the-badge)

<img src="assets/genial-logo-banner-dark.png" alt="Exemplo imagem">


> Repositório com os **materiais do curso “Genetic and Evolutionary Nature-Inspired Algorithms (GENIAL)”**, ministrado no **Laboratório de Inteligência de Dados (LID)** da **Universidade Federal do Pará (UFPA)**.  
Contém códigos, slides e notebooks utilizados durante as aulas práticas.

---

## 🎯 Objetivo do Curso

Compreender os **fundamentos teóricos e práticos da otimização bioinspirada**, explorando algoritmos e suas **aplicações em problemas reais de otimização combinatória**.

---

## 📚 Conteúdo Programático

### 1. Introdução à Otimização Bioinspirada
- Definição de problema, função objetivo e restrições  
- Métodos exatos e heurísticos  
- Meta-heurísticas e algoritmos bioinspirados  

### 2. Algoritmos Genéticos
- Inspiração na evolução biológica  
- Estrutura e operadores genéticos (seleção, cruzamento, mutação)  
- Aplicação: **otimização de horários de aulas**

### 3. Otimização por Colônia de Formigas
- Inspiração no comportamento coletivo de formigas  
- Estrutura do algoritmo e atualização de feromônio  
- Aplicação: **problema do caixeiro viajante**

### 4. Otimização por Enxame de Partículas
- Inspiração em bandos e cardumes  
- Atualização de velocidade e posição das partículas  
- Aplicação: **otimização de hiperparâmetros em redes neurais**

---

## 🧩 Estrutura do Repositório

```
├── assets/                       # Figuras utilizadas na construção das aulas
├── aulas/                        # Código Fonte
│ ├── aula_1_introducao.ipynb     # Conteúdo da aula de Introdução de Metaheuristica
│ ├── aula_2_ag.ipynb             # Conteúdo da aula de Algoritmo Genético
│ ├── aula_3_aco.ipynb            # Conteúdo da aula de Algoritmo de Colônia de Formiga
| ├── aula_4_pso.ipynb            # Conteúdo da aula de PSO
├── genial/                   
│ ├── ga.py                       # Script de Algoritmo Genético
│ ├── plots.py                    # Script de visualização e gráficos
│ ├── shc.py                      # Script de um simples Stochastic Hill Climbing optimizer
└── README.md
```

## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Linguagem de Programação `Python >= 3.11` Versão 
- Ambiente `Google Colab / Jupyter Notebook`. 
- Plataforma de Comunicação `Google Classroom`.

## 🚀 Instalando GENIAL

Para instalar o **GENIAL**, siga estas etapas:

Linux e macOS:

```bash
git clone git@github.com:lid-ufpa/genial.git
cd genial

```

Windows:

```PowerShell
git clone https://github.com/usuario/genial-workshop.git
cd genial-workshop
pip install -r requirements.txt
```

## ☕ Executando GENIAL

Para usar **GENIAL**, siga estas etapas:

### No Google Colab

1. Faça o upload do notebook desejado na sua conta do Google Drive.
2. Execute célula por célula conforme a explicação do notebook.

### Localmente (Jupyter)
```
jupyter notebook
```
Depois, abra o arquivo .ipynb da aula que deseja executar.

## 🧠 Metodologia

* Exposição teórica dos conceitos
* Atividades práticas em grupo
* Estudos de caso aplicados
* Projeto final integrando teoria e prática

## 📫 Contribuindo para GENIAL

Para contribuir com **GENIAL**, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin main`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## 🤝 Colaboradores

Agradecemos às seguintes pessoas que contribuíram para este projeto:

<table>
  <tr>
    <td align="center">
      <a href="#" title="Helder Matos">
        <img src="https://avatars.githubusercontent.com/u/17325561?v=4" width="100px;" alt="Foto do Helder Matos no GitHub"/><br>
        <sub><b>Helder Matos</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="https://lattes.cnpq.br/1659693816509187" title="Jean Carlos">
        <img src="https://avatars.githubusercontent.com/u/73586340?v=4" width="100px;" alt="Foto do Jean Carlos no GitHub"/><br>
        <sub><b>Jean Carlos</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="Marcos Araujo">
        <img src="https://avatars.githubusercontent.com/u/159856979?v=4" width="100px;" alt="Foto do Marcos Araujo no GitHub"/><br>
        <sub><b>Marcos Araujo</b></sub>
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="#" title="Eduardo Kohei">
        <img src="https://avatars.githubusercontent.com/u/133936439?v=4" width="100px;" alt="Foto do Eduardo Kohei no GitHub"/><br>
        <sub><b>Eduardo Kohei</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="Samara Souza">
        <img src="https://avatars.githubusercontent.com/u/77058376?v=4" width="100px;" alt="Foto da Samara Souza no GitHub"/><br>
        <sub><b>Samara Souza</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="Maria Siqueira">
        <img src="https://avatars.githubusercontent.com/u/208213340?v=4" width="100px;" alt="Foto da Maria Siqueira no GitHub"/><br>
        <sub><b>Maria Siqueira</b></sub>
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="#" title="Vitor Cardoso">
        <img src="https://avatars.githubusercontent.com/u/143220203?v=4" width="100px;" alt="Foto do Vitor Cardoso no GitHub"/><br>
        <sub><b>Vitor Cardoso</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="Aldrey Sandre">
        <img src="https://avatars.githubusercontent.com/u/165036139?v=4" width="100px;" alt="Foto do Aldrey Sandre no GitHub"/><br>
        <sub><b>Aldrey Sandre</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="Jeojildo Pereira">
        <img src="https://avatars.githubusercontent.com/u/132309605?v=4" width="100px;" alt="Foto do Jeojildo Pereira no GitHub"/><br>
        <sub><b>Jeojildo Pereira</b></sub>
      </a>
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="#" title="Marcos Vinicius">
        <img src="https://avatars.githubusercontent.com/u/82077382?v=4" width="100px;" alt="Foto do Marcos Vinicius no GitHub"/><br>
        <sub><b>Marcos Vinicius</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="Emilly Caroline">
        <img src="https://avatars.githubusercontent.com/u/93013035?v=4" width="100px;" alt="Foto da Emilly Caroline no GitHub"/><br>
        <sub><b>Emilly Caroline</b></sub>
      </a>
    </td>
    <td align="center">
      <a href="#" title="Izaac Junior">
        <img src="https://avatars.githubusercontent.com/u/213531460?v=4" width="100px;" alt="Foto do Izaac Junior no GitHub"/><br>
        <sub><b>Izaac Junior</b></sub>
      </a>
    </td>
  </tr>
</table>



## 😄 Seja um dos contribuidores

Quer fazer parte desse projeto? Clique [AQUI](CONTRIBUTING.md) e leia como contribuir.

## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.