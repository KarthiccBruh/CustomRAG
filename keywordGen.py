import json
from typing import Dict, List, Any
import spacy
from collections import Counter

class ResumeKeywordExtractor:
    def __init__(self):
        # Try to load the small English model
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading spaCy English model. This might take a few moments...")
            import subprocess
            subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
            self.nlp = spacy.load("en_core_web_sm")

    def extract_keywords(self, resume_data: Dict[str, Any]) -> Dict[str, List[str]]:
        """
        Extract and categorize keywords from different sections of the resume.
        
        Args:
            resume_data (Dict[str, Any]): Parsed resume data
        
        Returns:
            Dict[str, List[str]]: Categorized keywords
        """
        keywords = {
            'domain_keywords': [],
            'technical_skills': [],
            'certifications': [],
            'project_keywords': []
        }

        # Extract domain and technical keywords
        if resume_data.get('domain'):
            domain_doc = self.nlp(resume_data['domain'])
            keywords['domain_keywords'] = [
                token.text for token in domain_doc 
                if token.pos_ in ['NOUN', 'PROPN'] and not token.is_stop
            ]

        # Technical skills
        if resume_data.get('skills'):
            keywords['technical_skills'] = resume_data['skills']

        # Certifications
        if resume_data.get('achievements'):
            keywords['certifications'] = [
                cert for cert in resume_data.get('achievements', []) 
                if 'Certified' in cert
            ]

        # Project keywords
        if resume_data.get('specific_projects'):
            for project in resume_data.get('specific_projects', []):
                if project.get('description'):
                    proj_doc = self.nlp(project['description'])
                    project_keywords = [
                        token.text for token in proj_doc 
                        if token.pos_ in ['NOUN', 'VERB'] and not token.is_stop
                    ]
                    keywords['project_keywords'].extend(project_keywords)

        # Remove duplicates and clean up
        for key in keywords:
            keywords[key] = list(set(keywords[key]))

        return keywords
    
class KeywordExtractor:
    def __init__(self):
        try:
            import spacy
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading spaCy English model. This might take a few moments...")
            import subprocess
            subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
            self.nlp = spacy.load("en_core_web_sm")

    def extract_keywords(self, text: str) -> List[str]:
        """
        Extract the most relevant 7 total keywords from the given text. SHOULD BE ONLY MAX 7 KEYWORDS
        
        Args:
            text (str): The input text from which to extract keywords.
        
        Returns:
            List[str]: A list of Unique semantic meaning relevant keywords should be under 7 elements.
            
        """
        if not text:
            return []

        # Process the text
        doc = self.nlp(text)

        # Extract relevant keywords (nouns, proper nouns, verbs) excluding stopwords
        keywords = [
            token.text for token in doc 
            if token.pos_ in ["NOUN", "PROPN", "VERB"] and not token.is_stop
        ]

        # Remove duplicates and return
        return sorted(set(keywords[:5]))
    
    
def extractresume():
    # Open and load the JSON file directly
    with open('./json/Resume.json', 'r') as file:
        resume_data = json.load(file)
    
    # Extract keywords
    extractor = ResumeKeywordExtractor()
    keywords = extractor.extract_keywords(resume_data)
    
    return keywords

def extractans():
    # Open and load the JSON file directly
    with open('./json/data.json', 'r') as file:
        answer_data = json.load(file)
    
    # Extract keywords
    extractor = KeywordExtractor()
    keywords = extractor.extract_keywords(answer_data.get('dataa',''))
    
    return keywords

# print(ResumeKeywordExtractor())
# print(extractans())
hi=1