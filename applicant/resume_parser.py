import PyPDF2
import inline as inline
import textract
import itertools
import re
import string
import pandas as pd
import matplotlib.pyplot as plt


# Create dictionary with industrial and system engineering key terms by area
terms = {'Software Engineer': ['java', 'javascript', 'typescript', 'nodejs', 'golang', 'test driven development',
                               'agile', 'data structures', 'algorithms', 'reactjs', 'software development', 'git',
                               'python', 'linux',
                               'bash', 'programming', 'sql', 'agile methodologies',
                               'rust', 'elixir', 'web developer', 'backend developer',
                               'frontend developer', 'fullstack', 'aws', 'gcp', 'amazon web services',
                               'google cloud platform'],
         'DevOps Engineer': ['devops', 'docker', 'ansible', 'jenkins', 'kubernetes', 'aws', 'amazon web services',
                             'git', 'linux', 'scrum', 'terraform', 'microsoft azure', 'azure', 'agile', 'bash',
                             'continuous integration and continuous delivery (ci / cd)',
                             'continuous integration', 'ci', 'continuous delivery', 'cd', 'python',
                             'sql', 'java', 'shell scripting',
                             'cloud computing', 'elasticsearch', 'go', 'openstack', 'puppet', 'nginx',
                             'maven', 'chef', 'github', 'nagios', 'sonarqube', 'powershell', 'mysql',
                             'linux system administration', 'gitlab'],
         'UI/UX Engineer': ['user interface design', 'web design', 'bootstrap', 'css3', 'css', 'cascading stylesheets',
                            'adobe illustrator', 'html5', 'html', 'jquery',
                            'adobe photoshop', 'dreamweaver', 'responsive web design', 'javascript', 'graphic design',
                            'wordpress', 'user experience', 'ux',
                            'web development', 'blinds', 'logo design', 'user experience design', 'ued', 'adobe xd',
                            'sass', 'angularjs',
                            'front-end development', 'wireframing', 'interaction design', 'usability',
                            'usability testing'],
         'Backend Engineer': ['git', 'mysql', 'docker', 'mongodb', 'javascript', 'amazon web services', 'aws',
                              'node.js', 'nodejs', 'php', 'redis', 'java', 'spring framework', 'scrum', 'postgresql',
                              'python', 'sql', 'linux', 'cascading style sheets', 'css', 'symfony', 'jquery', 'html',
                              'go', 'golang', 'c++', 'back-end web development', 'c', 'software development', 'django',
                              'reactjs', 'react.js', 'laravel', 'angularjs', 'elasticsearch', 'express', 'rest apis',
                              'web development', 'microservices', 'c#', 'kubernetes', 'codeigniter', 'vue', 'ajax',
                              'representational state transfer', 'html5', 'maven', 'nosql', 'restful web services',
                              'json'],
         'Data analytics': ['analytics', 'api', 'aws', 'big data', 'busines intelligence', 'clustering', 'code',
                            'coding', 'data', 'database', 'data mining', 'data science', 'deep learning', 'hadoop',
                            'hypothesis test', 'iot', 'internet', 'machine learning', 'modeling', 'nosql', 'nlp',
                            'predictive', 'programming', 'python', 'r', 'sql', 'tableau', 'text mining',
                            'visualuzation'],
         'Frontend Engineer': ['front-end web development', 'frontend web development', 'frontend development', 'css',
                               'css3', 'cascading style sheets', 'html5', 'reactjs', 'react.js', 'jquery', 'sass',
                               'web development', 'bootstrap', 'tailwind css', 'tailwind', 'tailwindcss',
                               'responsive web design', 'wordpress', 'html', 'html5',
                               'web design', 'git', 'php', 'angularjs', 'adobe photoshop', 'nodejs', 'node.js',
                               'typescript', 'redux', 'mysql', 'postgresql', 'vue', 'vuejs', 'vue.js', 'webpack',
                               'github', 'laravel', 'react native', 'user experience (ux)', 'user experience', 'ux',
                               'gulp', 'gulp.js', 'gulpjs', 'scrum', 'adobe illustrator', 'web applications',
                               'user interface design'],
         'Fullstack Engineer': ['angularjs', 'javascript', 'back-end web development', 'back-end development',
                                'backend development', 'nodejs', 'node.js', 'css', 'css3', 'cascading style sheets',
                                'web development', 'mysql', 'jquery', 'full-stack development', 'fullstack development',
                                'html', 'html5', 'php', 'front-end web development', 'front-end development',
                                'frontend development', 'reactjs', 'react.js', 'bootstrap', 'tailwind', 'tailwindcss',
                                'aws', 'gcp', 'amazon web services', 'google cloud platform', 'docker',
                                'software development', 'java', 'vue', 'vuejs', 'postgresql', 'symfony',
                                'microservices', 'github', 'codeigniter', 'react native', 'c#', 'sass', 'express',
                                'django', 'redux', 'spring boot', 'scrum'],

         'Soft Skills': ['verbal and written communication', 'teamwork', 'leadership', 'time management', 'flexibility', 'patience', 'creativity', 'work ethic', 'attention to detail', 'detail oriented', 'adaptability', 'problem solving', 'discipline', 'motivated', 'autonomous', 'communication']
         }


def extract_text(path_to_file):
    # Open pdf file
    pdfFileObj = open(path_to_file, 'rb')

    # Read file
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # Get total number of pages
    num_pages = pdfReader.numPages

    # Initialize a count for the number of pages
    count = 0

    # Initialize a text empty string variable
    text = ""

    # Extract text from every page on the file
    while count < num_pages:
        pageObj = pdfReader.getPage(count)
        count += 1
        text += pageObj.extractText()

    return text


def clean_text(data):
    # Convert all strings to lowercase
    text = data.lower()

    # Remove numbers
    text = re.sub(r'\d+', '', text)

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    return text


def calculate_score(text):
    # Initialize score counters for each area
    software_engineer = 0
    found_software_keywords = []
    devops_engineer = 0
    found_devops_keywords = []
    ui_ux_engineer = 0
    found_ui_ux_keywords = []
    backend_engineer = 0
    found_backend_keywords = []
    data = 0
    found_analytics_keywords = []
    frontend_engineer = 0
    found_frontend_keywords = []
    fullstack_engineer = 0
    found_fullstack_keywords = []
    soft_skills = 0
    found_soft_skill_keywords = []

    # Create an empty list where the scores will be stored
    scores = []

    # Obtain the scores for each area
    for area in terms.keys():

        if area == 'Software Engineer':
            for word in terms[area]:
                if word in text:
                    software_engineer += 1
                    found_software_keywords.append(word)
            scores.append(software_engineer)

        elif area == 'DevOps Engineer':
            for word in terms[area]:
                if word in text:
                    devops_engineer += 1
                    found_devops_keywords.append(word)
            scores.append(devops_engineer)

        elif area == 'UI/UX Engineer':
            for word in terms[area]:
                if word in text:
                    ui_ux_engineer += 1
                    found_ui_ux_keywords.append(word)
            scores.append(ui_ux_engineer)

        elif area == 'Backend Engineer':
            for word in terms[area]:
                if word in text:
                    backend_engineer += 1
                    found_backend_keywords.append(word)
            scores.append(backend_engineer)

        elif area == 'Data analytics':
            for word in terms[area]:
                if word in text:
                    data += 1
                    found_analytics_keywords.append(word)
            scores.append(data)

        elif area == 'Frontend Engineer':
            for word in terms[area]:
                if word in text:
                    frontend_engineer += 1
                    found_frontend_keywords.append(word)
            scores.append(data)

        elif area == 'Soft Skills':
            for word in terms[area]:
                if word in text:
                    soft_skills += 1
                    found_soft_skill_keywords.append(word)
            scores.append(soft_skills)

        else:
            for word in terms[area]:
                if word in text:
                    fullstack_engineer += 1
                    found_fullstack_keywords.append(word)
            scores.append(fullstack_engineer)


    found_technical_keywords = list(set(itertools.chain(found_backend_keywords, found_software_keywords, found_devops_keywords, found_analytics_keywords, found_fullstack_keywords, found_ui_ux_keywords)))

    found_keywords = {
        'technical_skills': found_technical_keywords,
        'soft_skills': found_soft_skill_keywords
    }

    return scores, found_keywords


def summarize_resume(path):
    resume_data = extract_text(path)

    cleaned_data = clean_text(resume_data)

    scores = calculate_score(cleaned_data)[0]
    found_keywords = calculate_score(cleaned_data)[1]

    summary = pd.DataFrame(scores, index=terms.keys(), columns=['score']).sort_values(by='score', ascending=False)
    summary = summary.to_dict()
    result = {
        'backend': (summary['score']['Backend Engineer'] / sum(scores)) * 100,
        'software': (summary['score']['Software Engineer'] / sum(scores)) * 100,
        'devops': (summary['score']['DevOps Engineer'] / sum(scores)) * 100,
        'analytics': (summary['score']['Data analytics'] / sum(scores)) * 100,
        'fullstack': (summary['score']['Fullstack Engineer'] / sum(scores)) * 100,
        'ui_ux': (summary['score']['UI/UX Engineer'] / sum(scores)) * 100,
        'soft_skills': (summary['score']['Soft Skills'] / sum(scores)) * 100,
    }


    return {
        'candidate_profile': result,
        'candidate_keywords': found_keywords

    }

