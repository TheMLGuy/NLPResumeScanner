# NLPResumeScanner
Scan pdf format of resume and group similar resumes, identify common skillsets<br>
Usecase: Consider a large set of resumes that have been received for various positions at a firm but are not classified according to the<br> position, can apply NLP for identifing and classifying resumes to particular job roles. <br>
Goals to achieve:<br>
Parse resumes<br>
Build entity relations<br>
Classify resumes according to domains<br>
identify skillsets that are common per domain<br>
Visualize using Javascript<br>




Setting up Environment from scratch:  
    conda create --name NLPResumeScanner        # creates new environment this project
    Source activate NLPResumeScanner            # activate the environment
    python -m ipykernel install --user --name NLPResumeScanner   # set the new kernel
    [Get help on install](http://ipython.readthedocs.io/en/stable/install/kernel_install.html)

    pip install -U nltk             # to install nltk module
    python -m nltk.downloader all   # to download the nltk data
    pip install PyPDF2
