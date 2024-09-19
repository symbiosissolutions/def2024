import os
from pydantic import BaseModel, Field
from pydantic.types import List

from crawl4ai import WebCrawler
from crawl4ai.extraction_strategy import LLMExtractionStrategy


class EducationalResourceModel(BaseModel):
    title: str = Field(..., description="Title of the lesson plan or educational resource (e.g., 'Grade 4: Unit 1 - Actions Speak Louder Than Words: Lesson 1').")
    subject: str = Field(..., description="The academic subject associated with the resource (e.g., 'English Language Arts').")
    grade_level: str = Field(..., description="The target grade level for which the resource is intended (e.g., 'Grade 4').")
    material_type: str = Field(..., description="The type of material provided (e.g., 'Lesson Plan').")
    authors: List[str] = Field(..., description="List of authors or contributors who created the resource (e.g., 'Shannon Copeland, Lauren Byrd, MSDE Admin, Jennifer Ralston').")
    date_added: str = Field(..., description="The date on which the resource was added to the platform (e.g., '06/27/2018').")
    license: str = Field(..., description="The type of license that governs the usage of the resource (e.g., 'Creative Commons Attribution Non-Commercial Share Alike').")
    overview: str = Field(..., description="A brief summary or description of the lesson plan, its content, and learning objectives.")
    language: str = Field(..., description="The language in which the resource is written (e.g., 'English').")
    standards: List[str] = Field(..., description="The educational standards that align with the resource (e.g., 'Wyoming Standards for English Language Arts, Grade 4').")
    reviewers: List[str] = Field(..., description="Organizations or individuals who reviewed or endorsed the resource (e.g., 'Maryland State Department of Education').")


def create_crawler():
    crawler = WebCrawler(verbose=True)
    crawler.warmup()
    return crawler


crawler = create_crawler()


# Run the crawler on a URL
result = crawler.run(
    url="https://oercommons.org/courseware/lesson/25047",
    extraction_strategy=LLMExtractionStrategy(
        provider="groq/llama-3.1-70b-versatile",
        api_token=os.getenv('GROQ_API_KEY'),
        schema=EducationalResourceModel.schema(),
        extraction_type="schema",
        instruction="""From the given content, extract information related
        to an educational resource. The extracted data should include the
        following fields: title, subject, grade_level, material_type, authors,
        date_added, license, overview, language, standards, and reviewers.
        Ensure that each extracted resource is formatted as a JSON object.
        For each resource you find, ensure the fields are populated correctly
        based on the content provided. If any information is missing, leave
        the corresponding field out of the JSON output."""
    ),
    bypass_cache=True,
)

# Print the extracted content
print(result.extracted_content)


"""Example Result

[
    {
        "title": "2022 OER Partner Summit",
        "subject": "",
        "grade_level": "",
        "material_type": "",
        "authors": "",
        "date_added": "",
        "license": "",
        "overview": "",
        "language": "",
        "standards": "",
        "reviewers": "",
        "error": false
    },
    {
        "title": "Open Textbooks",
        "subject": "",
        "grade_level": "",
        "material_type": "",
        "authors": "",
        "date_added": "",
        "license": "",
        "overview": "",
        "language": "",
        "standards": "",
        "reviewers": "",
        "error": false
    },
    {
        "title": "#GoOpen",
        "subject": "",
        "grade_level": "",
        "material_type": "",
        "authors": "",
        "date_added": "",
        "license": "",
        "overview": "",
        "language": "",
        "standards": "",
        "reviewers": "",
        "error": false
    },
    {
        "title": "Professional Learning",
        "subject": "",
        "grade_level": "",
        "material_type": "",
        "authors": "",
        "date_added": "",
        "license": "",
        "overview": "",
        "language": "",
        "standards": "",
        "reviewers": "",
        "error": false
    },
    {
        "title": "Climate Education",
        "subject": "",
        "grade_level": "",
        "material_type": "",
        "authors": "",
        "date_added": "",
        "license": "",
        "overview": "",
        "language": "",
        "standards": "",
        "reviewers": "",
        "error": false
    },
    {
        "title": "OERizona",
        "subject": "",
        "grade_level": "",
        "material_type": "",
        "authors": "",
        "date_added": "",
        "license": "",
        "overview": "",
        "language": "",
        "standards": "",
        "reviewers": "",
        "error": false
    },
    {
        "title": "Adult Education Open Community of Resources",
        "subject": "",
        "grade_level": "",
        "material_type": "",
        "authors": "",
        "date_added": "",
        "license": "",
        "overview": "",
        "language": "",
        "standards": "",
        "reviewers": "",
        "error": false
    },
    {
        "title": "OpenStax Biology 2e",
        "subject": "",
        "grade_level": "",
        "material_type": "",
        "authors": "",
        "date_added": "",
        "license": "",
        "overview": "",
        "language": "",
        "standards": "",
        "reviewers": "",
        "error": false
    },
    {
        "title": "PA STEM Toolkit",
        "subject": "",
        "grade_level": "",
        "material_type": "",
        "authors": "",
        "date_added": "",
        "license": "",
        "overview": "",
        "language": "",
        "standards": "",
        "reviewers": "",
        "error": false
    },
    {
        "title": "Pathways Project | Language Teaching Repository @ Boise State",
        "subject": "",
        "grade_level": "",
        "material_type": "",
        "authors": "",
        "date_added": "",
        "license": "",
        "overview": "",
        "language": "",
        "standards": "",
        "reviewers": "",
        "error": false
    },
    {
        "title": "Student Advocacy",
        "subject": "",
        "grade_level": "",
        "material_type": "",
        "authors": "",
        "date_added": "",
        "license": "",
        "overview": "",
        "language": "",
        "standards": "",
        "reviewers": "",
        "error": false
    },
    {
        "subject": "Applied Science, Arts and Humanities, Business and Communication, Career and Technical Education, Education, English Language Arts, History, Law, Life Science, Mathematics, Physical Science, Social Science",
        "standards": [
            "AAAS 2008 Standards",
            "AASL 21st Century Learner Standards 2007",
            "AASL National School Library Standards for Learners, School Librarians and School Libraries",
            "AASL Standards for Initial Preparation of School Librarians 2007",
            "C3 Framework for Social Studies",
            "CSTA K-12 Computer Science Standards",
            "Common Core State Standards English Language Arts",
            "Common Core State Standards Math",
            "Florida ELA B.E.S.T. Standards",
            "Florida Mathematics",
            "Florida Science Standards",
            "Georgia ELA Standards of Excellence",
            "Georgia Math Standards of Excellence",
            "Georgia Science Standards of Excellence",
            "Iowa Core 21st Century Skills",
            "Iowa Core in Social Studies",
            "MADA ICT-AID Competency Framework",
            "Maryland College and Career Ready English Language Arts Standards",
            "Maryland College and Career Ready Math Standards",
            "Minnesota ELA Standards",
            "Minnesota Math Standards",
            "Minnesota Science Standards",
            "Missouri Learning Standards - Mathematics",
            "Missouri Learning Standards - Science",
            "Nebraska Agriculture and Natural Resources Standards",
            "Nebraska Business, Marketing and Management Standards",
            "Nebraska Business, Marketing and Management Standards 2022",
            "Nebraska Communication and Information Systems Standards",
            "Nebraska Communication and Information Systems Standards 2022",
            "Nebraska Family and Consumer Science Standards",
            "Nebraska Health Science Standards",
            "Nebraska Human Sciences and Education 2022",
            "Nebraska K-12 Fine Arts Standards",
            "Nebraska Physical Education Standards",
            "Nebraska Skilled & Technical Sciences Standards",
            "Nebraska Skilled and Technical Sciences 2022",
            "Nebraska World Language Standards",
            "Nebraska's College and Career Ready Standards for English Language Arts",
            "Nebraska's College and Career Ready Standards for Math",
            "Nebraska's College and Career Ready Standards for Science",
            "Nebraska's Social Studies Standards",
            "New Hampshire State Science Standards",
            "Next Generation Science Standards",
            "North Carolina English Language Arts Standards",
            "North Carolina Essential Standards for Science",
            "North Carolina Math Standards",
            "North Dakota Dance Content Standard",
            "North Dakota English Language Arts & Literacy Content Standards",
            "North Dakota Mathematics Content Standards",
            "North Dakota Media Arts Standards",
            "Oregon Art Standards",
            "Oregon CTE Standards",
            "Oregon English Language Arts and Literacy",
            "Oregon English Language Proficiency Standards",
            "Oregon Health Education Standards",
            "Oregon Mathematics Standards",
            "Oregon Physical Education Standards",
            "Oregon Science Standards",
            "Oregon Social Sciences Standards",
            "Oregon World Languages",
            "Pennsylvania Academic Standards for Environment and Ecology",
            "Pennsylvania Academic Standards for Science and Technology (2002)",
            "Pennsylvania Core Standards for English Language Arts",
            "Pennsylvania Core Standards for Mathematics",
            "Pennsylvania Standards for Business, Computer and Information Technology",
            "Pennsylvania Standards for Career Education and Work",
            "Pennsylvania Standards for Civics and Government",
            "Pennsylvania Standards for Economics",
            "Pennsylvania Standards for Family and Consumer Sciences",
            "Pennsylvania Standards for Geography",
            "Pennsylvania Standards for Health, Safety & Physical Education",
            "Pennsylvania Standards for History",
            "Pennsylvania Standards for Science and Technology and Engineering Education",
            "Texas Essential Knowledge and Skills for English Language Arts and Reading",
            "Texas Essential Knowledge and Skills for Math",
            "Texas Essential Knowledge and Skills for Science",
            "UNESCO ICT Competency Framework",
            "Virginia English Standards of Learning",
            "Virginia Mathematics Standards of Learning",
            "Virginia Science Standards of Learning 2018",
            "Washington Arts Standards",
            "Washington Educational Technology Standards",
            "Washington Environmental and Sustainability Education Standards",
            "Washington Financial Education Standards",
            "Washington Health Standards",
            "Washington Physical Education Standards",
            "Washington Social Emotional Learning Standards",
            "Washington Social Studies Standards",
            "Wyoming Career and Vocational Education Content Standards",
            "Wyoming Fine and Performing Arts Content Standards",
            "Wyoming Foreign Languages Content Standards",
            "Wyoming Health Education Content Standards",
            "Wyoming Physical Education Content Standards",
            "Wyoming Science Content and Performance Standards",
            "Wyoming Social Studies Content Standards",
            "Wyoming Standards for English Language Arts",
            "Wyoming Standards for Mathematics",
            "\u0625\u0637\u0627\u0631 \u0639\u0645\u0644 \u0645\u062f\u0649 \u0644\u062a\u0646\u0645\u064a\u0629 \u0627\u0644\u0643\u0641\u0627\u0621\u0627\u062a"
        ],
        "error": false
    },
    {
        "title": "Grade 4: Unit 1- Actions Speak Louder Than Words: Lesson 1",
        "subject": "English Language Arts",
        "grade_level": "Grade 4",
        "material_type": "Lesson Plan",
        "authors": [],
        "overview": "This lesson opens the unit and prepares learners for the structure of the instructional routines. The anchor text for this lesson is, Words Set Me Free by Lesa Cline-Ransome. This literary nonfiction text chronicles the story of Frederick Douglass' early life and includes events that influenced both his life and those of others. The students should listen for examples of how actions speak louder than words. The initial read will allow students an opportunity to comprehend on a literal level. The subsequent readings provide opportunities for students to analyze and interpret figurative language throughout the book. Specifically, the students will identify how similes and metaphors enhance the reader's understanding of the life of Frederick Douglass. Students will routinely write in a response log to demonstrate understanding of the theme of this unit, Actions Speak Louder than Words. In addition, students will use their knowledge of figurative language in their writing.",
        "error": false
    },
    {
        "title": "",
        "subject": "English Language Arts",
        "grade_level": "Grade 4",
        "material_type": "",
        "authors": [
            "Shannon Copeland",
            "Lauren Byrd",
            "MSDE Admin",
            "Jennifer Ralston"
        ],
        "date_added": "06/27/2018",
        "license": "Creative Commons Attribution Non-Commercial Share Alike",
        "language": "English",
        "standards": [
            "WY.ELA-Literacy.L.4.5b",
            "WY.ELA-Literacy.RI.4.1",
            "WY.ELA-Literacy.RI.4.5",
            "WY.ELA-Literacy.SL.4.1",
            "WY.ELA-Literacy.RI.4.3",
            "MCCRS.ELA-Literacy.L.4.5b",
            "MCCRS.ELA-Literacy.RI.4.1"
        ],
        "reviewers": [
            "Maryland State Department of Education"
        ],
        "error": false
    },
    {
        "title": "Grade 4: Unit 1 - Actions Speak Louder Than Words: Lesson 1",
        "subject": "English Language Arts",
        "grade_level": "Grade 4",
        "material_type": "Lesson Plan",
        "standards": [
            "MCCRS.ELA-Literacy.RI.4.5",
            "MCCRS.ELA-Literacy.SL.4.1",
            "MCCRS.ELA-Literacy.RI.4.3",
            "CCSS.ELA-Literacy.RI.4.1",
            "CCSS.ELA-Literacy.RI.4.5",
            "CCSS.ELA-Literacy.L.4.5b",
            "CCSS.ELA-Literacy.RI.4.3",
            "CCSS.ELA-Literacy.SL.4.1"
        ],
        "reviewers": [
            "Maryland State Department of Education"
        ],
        "error": false
    }
]
"""