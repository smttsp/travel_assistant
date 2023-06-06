import glob
import os
from pprint import pprint

import openai

from utils.file_utils import read_text_from_file


openai.api_key = os.getenv("OPENAI_API_KEY")


def get_content_from_inputs(resume_file):
    # resume_file = '/users/samettaspinar/desktop/resumes/Samet_resume.pdf'
    # resume_file = "/users/samettaspinar/desktop/resumes/resume2.doc"
    # jd_file = "/users/samettaspinar/desktop/jd/cellino_jd.pdf"

    # jd_link = "https://recruiterflow.com/db_74f6835629d4836e1f3120b2162e6337/jobs/79"
    # get_text_from_html(link)
    # jd = jd_main(jd_link)

    resume_content = read_text_from_file(resume_file)

    # content = (
    #     f"Given that my resume_file is: {resume_content} \n\n"
    #     f"and job description I am applying is {jd_content}.\n\n"
    #     "Can you write me a cover letter"
    # )
    # return content




if __name__ == "__main__":
    resume_folder = "/users/samettaspinar/desktop/resumes/"

    query = (
        "can you give me 5 touristic places near boston in a csv format as:"
        "``` name_of_location | lattitude | longitude | city | state | country | zip code ```" 
        "can you give this output as csv? no need to show the code to generate the csv file"
    )
    print(query)

    from utils.chatgpt_utils import get_location_csv
    get_location_csv(query)