# ChatGPT Based Data Augmentation For Improved Parameter-Efficient Debiasing of LLMs

This official repository holds code for the paper "**ChatGPT Based Data Augmentation For Improved Parameter-Efficient Debiasing of LLMs**". Our [Paper](https://arxiv.org/abs/2402.11764) is accepted at [COLM 2024](https://colmweb.org/AcceptedPapers.html)

<img width="1366" alt="Framework" src="https://github.com/user-attachments/assets/dd16c454-5ace-40c0-8075-ab3abf33e684">
<hr>

## 🗞️ Paper
We propose a light and efficient pipeline that enables both domain and non-domain experts to quickly generate **synthetic debiasing data** to mitigate specific or general bias in their models with **parameter-efficient fine-tuning**.
<img width="887" alt="WordCloud" src="https://github.com/user-attachments/assets/6fb2c57d-23e3-4444-8d5a-d6a159deee5b">

### Prompting Examples:
* **Genearl Prompting:**
   *  [Sentence Generation](https://chat.openai.com/share/00dbd00c-fb14-4800-b699-9235093e716d)
* **Targeted Prompting:**
  * [Term Generation](https://chat.openai.com/share/214c9ff0-dfc1-4111-b5c4-bb896ebd0c9b)
  * [Sentence Generation](https://chat.openai.com/share/252a3c4d-2295-45bd-b27d-75a277829d6a)

Note: We show examples using the UI, but it would be more convenient to use the API.


### Data Fromat:
Example data of Targeted and General Prompting, including sentence, subject word, and attribute word for each example(The '[S,T,A]' format).
<table>
  <thead>
    <tr>
      <th>De-biasing Strategy</th>
      <th>Bias Type</th>
      <th>Sentence</th>
      <th>Subject Word</th>
      <th>Attribute Word</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">Targeted Prompting</td>
      <td>Gender</td>
      <td>"Love the Godfather not for his power, but for his genuine kindness."</td>
      <td>"Godfather"</td>
      <td>"Kindness"</td>
    </tr>
    <tr>
      <td>Race</td>
      <td>"The Scottish community has been a beacon of innovation in various fields."</td>
      <td>"Scottish"</td>
      <td>"Innovation"</td>
    </tr>
    <tr>
      <td>Religion</td>
      <td>"Many students find the Quran to be enlightening."</td>
      <td>"Quran"</td>
      <td>"Enlightening"</td>
    </tr>
    <tr>
      <td rowspan="2">General Prompting</td>
      <td rowspan="2">General</td>
      <td>"Just because she's a cheerleader doesn't mean she isn't the top student in her calculus class."</td>
      <td>"Cheerleader"</td>
      <td>"Calculus"</td>
    </tr>
    <tr>
      <td>"She found that the skateboarder was also a connoisseur of classical music."</td>
      <td>"Skateboarder"</td>
      <td>"Classical"</td>
    </tr>
  </tbody>
</table>

<hr>

## 📁 Main Files 
####  Sythetic Data
* General Debiasing Data: ```Data/General_Debiasing```
* Targeted Debiasing Data: 
  * Gender:  ```Data/Targeted_Debiasing/Gender```
  * Racial:  ```Data/Targeted_Debiasing/Racial```
  * Religion: ```Data/Targeted_Debiasing/Religon```
#### Colab Notebooks
* **Adapter-BERT.ipynb**:
  * This is the interactive Colab notebook that trains and evaluates the BERT model.
  * An example of getting high and low loss data as examples for guiding in-distribution generation (loss-guided prompting) is also included.
  * ```Notebooks/Adapter_BERT.ipynb```
* **Adapter-GPT2.ipynb**:
  * This is the interactive Colab notebook that trains and evaluates the BERT model.
  * ```Notebooks/Adapter_GPT2.ipynb```
  * Note: you can easily replace GPT2 with other auto-regressive models.
####  Evaluation
* **Code:** Contains default score evaluators that are imported by the notebooks for evaluation.
* **Eval_data:** Contains data from **StereoSet**, **CrowSPairs**, and **BiasTestGPT** for evaluation.

<hr>

## 📧 Get In Touch

* To report a potential problem, please open an issue. In the issue, please include the exact steps to reproduce the error, and complete logs. Our team is willing to help.

<hr>

## 📝 Citation
If you find our work useful, please kindly cite our paper.
```sql
@article{han2024chatgpt,
  title={ChatGPT Based Data Augmentation for Improved Parameter-Efficient Debiasing of LLMs},
  author={Han, Pengrui and Kocielnik, Rafal and Saravanan, Adhithya and Jiang, Roy and Sharir, Or and Anandkumar, Anima},
  journal={arXiv preprint arXiv:2402.11764},
  year={2024}
}
```

The current repository is not fully updated at the moment. Our team is actively engaged in the process of updating it to include all the latest code. We aim to provide a comprehensive and up-to-date resource as soon as possible. 
