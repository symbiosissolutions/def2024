# College Search ETL Pipeline

## Revolutionizing College Search with AI-Powered Assistance

This project focuses on developing an ETL (Extract, Transform, Load) pipeline using `requests` and `BeautifulSoup` to scrape data from [Edusanjal](https://edusanjal.com/), a college aggregator website. The goal is to create a comprehensive dataset that enables innovative solutions to provide personalized college recommendations.

## Background

Selecting the right college is often overwhelming for students due to the vast amount of information they need to consider—ranging from course offerings and faculty expertise to campus amenities and financial aid options. While AI has the potential to simplify this decision-making process through personalized recommendations, it requires access to detailed and comprehensive data about educational institutions.

## Project Objectives

- **Data Extraction**: Scrape detailed profiles of colleges and universities, including information on courses, faculty, admission processes, and more.
- **Data Transformation**: Clean and structure the scraped data to make it suitable for storage.
- **Data Loading**: Store the processed data in a format that can be easily accessed.

## Example Data

```json
{
  "college_name": "Thames International College",
  "location": {
    "address": "Surya Bikram Gyawali Marg, Old Baneshwor, Kathmandu",
    "map_coordinates": {
      "latitude": 27.701667450376043,
      "longitude": 85.34187196479105
    }
  },
  "contact_information": {
    "phone": "01-5971224",
    "email": "info@thamescollege.edu.np",
    "website": "http://www.thamescollege.edu.np",
    "social_media": {
      "youtube": "https://www.youtube.com/channel/UCCrnNV4hi0Lu6WVKQnrpUMg"
    }
  },
  "affiliation": "Tribhuvan University",
  "ownership": "Private Institution",
  "offered_programs": [
    {
      "name": "Bachelor of Business Administration (BBA)",
      "seats": 64
    },
    {
      "name": "Bachelor of Information Management (BIM)",
      "seats": 64
    },
    {
      "name": "Bachelor of Arts in Social Work (BASW)",
      "seats": 32
    },
    {
      "name": "Bachelor in Business Studies (BBS)",
      "seats": null
    },
    {
      "name": "Bachelor of Computer Application (BCA)",
      "seats": 35
    },
    {
      "name": "Bachelor of Business Management (BBM)",
      "seats": 45
    },
    {
      "name": "Bachelor of Arts in Psychology (BPSy)",
      "seats": null
    },
    {
      "name": "Bachelor of Arts in Rural Development (BRD)",
      "seats": null
    },
    {
      "name": "Bachelor of Arts in Journalism and Mass Communication (BAJM)",
      "seats": null
    },
    {
      "name": "Bachelor of Arts in Sociology",
      "seats": null
    },
    {
      "name": "Master of Business Studies (MBS)",
      "seats": null
    }
  ],
  "salient_features": {
    "project_work_and_field_visit": "The college maximizes learning through project work, seminar, and field visit in order to enhance both the theoretical and practical knowledge of the subject matter and the outer world.",
    "library": "The college is equipped with a rich library with plenty of reference materials, prescribed books and professional journals and magazines along with daily newspapers.",
    "labs": "TCMIT prides upon its well-equipped physics, chemistry, biology labs with the availability of all required equipment. Moreover, the college feels proud of its spacious computer lab which has been facilitated with an Internet connection to enable students to accomplish their researches efficiently.",
    "assessments": "Regular internal assessment tests will be routinely conducted to find out the strengths and weaknesses of the students so that remedial teaching can be carried out to enhance individual potentiality. Those who become absent or fail in the exam are bound to pay the fine as per the college's rule and sit for the re-exam.",
    "sports_and_cultural_programs": "Texas facilitates students to participate in a wide range of athletic activities including basketball, volleyball, table tennis, badminton, etc. Texas College also organizes various cultural programs with the presence of national celebrities.",
    "transportation": "Texas provides easy and comfortable transportation facility to its students who wish to receive the college transportation facility.",
    "social_service": "Texas encourages the dynamic modern youths to get intensively involved in various social and cultural works like blood donation, youth rehabilitation, cleaning campaign, traffic awareness campaign, charity and donation that make them really humans.",
    "appreciative_inquiry": "Texas focuses on the disciplined student with dignity. For this, special sessions on personality development and value education along with positive psychology will be conducted with the presence of renowned national and international experts."
  },
  "scholarships": "Chairman's  Merit  Scholarship  (For all Programs)\nThe Chairman's Merit Scholarship is a comprehensive award for outstanding newcomers who enroll in any of the undergraduate programs offered at Thames. The scholarship is renewable throughout the program.\n\nApplicants must meet the following criteria to apply:\n\nAchieved a minimum CGPA of 3.5/4.0 (or 75%) in 10th Grade from any recognized board.\n\nAchieved a minimum CGPA of 3.5/4.0 (or 75%) in 11th Grade (if the 12th-grade results are not published yet at the time of application.) Or,\n\nAchieved a minimum CGPA of 3.5/4.0 (or 75%) in 12th Grade (if the 12th-grade results have been already published at the time of application)\n\nTo be considered for the Chairman's Merit Scholarship Award, applicants must submit the following materials:\n\nCompleted Application form for Admission.\nCompleted Chairman's Merit Scholarship Application Form\nTerms of Scholarship\n\nScholarship awarded will be canceled if the student fails to meet the requirements listed below. \n\nAwardees must pass in all courses every semester.\nAwardees must maintain a minimum of 80 percent of attendance every semester.\nAwardees must maintain a minimum Semester GPA of 3.0/4.0\nAwardees must not be subject to any disciplinary action by the college\nScholarship once canceled cannot be reinstated under any circumstance.\n\nChairman's Merit Scholarship Award Application\n\nFor your application for Chairman's Merit Scholarship Award, please provide us with a brief statement indicating what you have gained from your involvement in the extracurricular activities and how you would continue your leadership involvement in Thames. Recommended length is 250-300 words. Please note that students who have achieved 3.5 GPA in your S.E.E and Higher Secondary Education are only eligible to apply for this scholarship.\n\nAspiring Entrepreneur Scholarship (For BBM)\nThe Aspiring Entrepreneur Scholarship Award was created to encourage entrepreneurship in a new generation of students. Students who wish to pursue an undergraduate studies in entrepreneurship (Bachelor of Business Management –Entrepreneurship) and are in need of financial support can apply for this scholarship.\n\nApplicants must meet the following criteria to apply:\n\nAchieved a minimum CGPA of 2.75/4.0 (or 60%) in 10th Grade from any recognized board.\nAchieved a minimum CGPA of 2.75/4.0 (or 60%) in 11th Grade (if the 12th-grade results are not published yet at the time of application.) Or,\nAchieved a minimum CGPA of 2.75/4.0 (or 60%) in 12th Grade (if the 12th-grade results have been already published at the time of application).\nTo be considered for the Aspiring Entrepreneur Award, applicants must submit the following materials:\n\nCompleted Application form for Admission in BBM.\nCompleted Aspiring Entrepreneur Scholarship Application Form\nTerms of Scholarship\n\nScholarship awarded will be canceled if the student fails to meet the requirements listed below. \n\nAwardees must pass in all courses every semester.\nAwardees must maintain a minimum of 80 percent of attendance every semester.\nAwardees must maintain a minimum Semester GPA of 2.75/4.0\nAwardees must not be subject to any disciplinary action by the college\nScholarship once canceled cannot be reinstated under any circumstance.\n\nAspiring Entrepreneur Scholarship Award Application\n\nFor your application for Aspiring Entrepreneur Scholarship Award, please provide us with a brief statement indicating what you have gained from your involvement in the extracurricular activities and how you would continue your leadership involvement in Thames. Recommended length is 250-300 words. \n\nInformation Technology Scholarship Award (For BCA and BIM)\nInformation Technology Scholarship Award was created to encourage the study of information technology to fulfill the ever-growing market demand for Information technology graduates. Students who wish to pursue an undergraduate studies in Information Technology (Bachelor of Computer Application or Bachelor of Information Management) and are in need of financial support can apply for this scholarship.\n\nApplicants must meet the following criteria to apply:\n\nAchieved a minimum CGPA of 2.75/4.0 (or 60%) in 10th Grade from any recognized board.\nAchieved a minimum CGPA of 2.75/4.0 (or 60%) in 11th Grade (if the 12th-grade results are not published yet at the time of application.) Or,\nAchieved a minimum CGPA of 2.75/4.0 (or 60%) in 12th Grade (if the 12th-grade results have been already published at the time of application).\nTo be considered for the Aspiring Entrepreneur Award, applicants must submit the following materials:\n\nCompleted Application form for Admission in BCA or BIM\nCompleted Information Technology Scholarship Award Application Form\nTerms of Scholarship\n\nScholarship awarded will be canceled if the student fails to meet the requirements listed below. \n\nAwardees must pass in all courses every semester.\nAwardees must maintain a minimum of 80 percent of attendance every semester.\nAwardees must maintain a minimum Semester GPA of 2.75/4.0\nAwardees must not be subject to any disciplinary action by the college\nScholarship once canceled cannot be reinstated under any circumstance.\nInformation Technology Scholarship Award Application\n\nFor your application for Information Technology Scholarship Award, please provide us with a brief statement indicating what you have gained from your involvement in the extracurricular activities and how you would continue your leadership involvement in Thames. Recommended length is 250-300 words. \n\nThames Need Based Scholarship ( For all programs )\nThames Need-Based Scholarship Award is awarded by the college to the incoming students who are seeking pursue undergraduate degree in any of the programs offered by Thames International College.This scholarship is renewable throughout the program.\n\nApplicants must meet the following criteria to apply:\n\nMust be from a low-income family (less than NRs.500,000 per year)\nAchieved a minimum CGPA of 2.75/4.0 (or 60%) in 10th Grade from any recognized board.\nAchieved a minimum CGPA of 2.75/4.0 (or 60%) in 11th Grade (if the 12th-grade results are not published yet at the time of application). Or,\nAchieved a minimum CGPA of 2.75/4.0 (or 60%) in 12th Grade (if the 12th grade results have been already published at the time of application.)\nTo be considered for the Thames Need-Based Scholarship Award, applicants must submit the following materials:\n\n Completed Application form for Admission.\n Completed SOSS Need-Based Scholarship Application Form\nTerms of Scholarship\n\nScholarship awarded will be canceled if the student fails to meet the requirements listed below. \n\nAwardees must pass in all courses every semester.\nAwardees must maintain a minimum of 80 percent of attendance every semester.\nAwardees must maintain a minimum Semester GPA of 2.5/4.0\nAwardees must not be subject to any disciplinary action by the college\nScholarship once canceled cannot be reinstated under any circumstance.\n\nThames Need Based Scholarship\n\nFor your application for Thames Need Based Scholarship, please provide a brief statement indicating your reasons for applying for financial assistance and why you should be awarded this scholarship.  Please note that students who have achieved 2.75 GPA in your SEE and Higher Secondary Education are only eligible to apply for this scholarship. Recommended length is 250-300 words. \n\nThames Full Tuition Waiver Scholarship Award ( for all programs)\n\nThames Full Tuition Waiver Scholarship is awarded to students whose family income is very low and cannot afford to continue their education without substantial financial support. This scholarship is for throughout the program. \n\nApplicants must meet the following criteria to apply:\n\nShould be from a low-income family (less than NRs.500,000 per year)\nShould have attended Government  School for his/her 10th, 11th, and 12th grade\nAchieved a minimum CGPA of 2.75/4.0 (or 50%) in 10th grade from any recognized board.\nAchieved a minimum CGPA of 2.75/4.0 (or 50%) in 11th grade and 12th grade.\nTo be considered for the Thames Full Tuition Waiver Scholarship Award, applicants must submit the following materials:\n\nCompleted Application form for Admission.\nCompleted Thames Full Tuition Waiver Scholarship Application Form\nTerms of Scholarship\n\nScholarship awarded will be canceled  if the student fails to meet the requirements listed below. \n\nAwardees must pass in all courses every semester.\nAwardees must maintain a minimum of 80 percent of attendance every semester.\nAwardees must maintain a minimum Semester GPA of 2.5/4.0\nAwardees must not be subject to any disciplinary action by the college\nScholarship once canceled cannot be reinstated under any circumstance.\n\nFull Tuition Waiver Scholarship Award\nFor your a Full Tuition Waiver Scholarship Award application, please provide a brief statement indicating your reasons for applying for financial assistance and why you should be awarded this scholarship.  Please note that students who have achieved 2.75 GPA in your S.E.E and Higher Secondary Education are only eligible to apply for this scholarship. Recommended length is 250-300 words\n\nEarly Bird Scholarship\nLeap ahead of your peers by applying early! With our Early Bird Scholarship, you can showcase your proactive approach and secure up to Rs 40,000 in financial support. Don't miss this opportunity to stand out and make your mark at Thames College.\n\nWork Study Program\nGain practical experience and earn while you learn through our exciting Work Study Program. Immerse yourself in real-world projects, expand your skill set, and receive financial support. We believe in providing a holistic education combining classroom learning and hands-on experience.\n\nSmart Saving Scheme\nGain the ultimate financial advantage by paying the total fee upfront and unlock an exclusive 15% discount. Take control of your educational investment and enjoy significant savings with this limited-time offer.",
  "images": [
    {
      "title": "Student Outdoor activities",
      "image_url": "https://media.edusanjal.com/__sized__/gallery/Thames_International_College_Activities_49-crop-c0-5__0-5-180x120-70.jpg"
    },
    {
      "title": "Sports at Thames International College",
      "image_url": "https://media.edusanjal.com/__sized__/gallery/Thames_International_College_Activities_47-crop-c0-5__0-5-180x120-70.jpg"
    },
    {
      "title": "Student Activities at Thames International College",
      "image_url": "https://media.edusanjal.com/__sized__/gallery/Thames_International_College_Activities_45-crop-c0-5__0-5-180x120-70.jpg"
    },
    {
      "title": "Student Activities at Thames International College",
      "image_url": "https://media.edusanjal.com/__sized__/gallery/Thames_International_College_Activities_44-crop-c0-5__0-5-180x120-70.jpg"
    },
    {
      "title": "Thames Class Room",
      "image_url": "https://media.edusanjal.com/__sized__/gallery/Thames_Class_Room-crop-c0-5__0-5-180x120-70.jpg"
    },
    {
      "title": "Thames Building",
      "image_url": "https://media.edusanjal.com/__sized__/gallery/Thames_Building-crop-c0-5__0-5-180x120-70.jpg"
    },
    {
      "title": "Student Life at Thames",
      "image_url": "https://media.edusanjal.com/__sized__/gallery/Thames_Students-crop-c0-5__0-5-180x120-70.jpg"
    },
    {
      "title": "Library at Thames",
      "image_url": "https://media.edusanjal.com/__sized__/gallery/Thames_Library-crop-c0-5__0-5-180x120-70.jpg"
    },
    {
      "title": "Winners of the Thames Inter College Cricket 2014",
      "image_url": "https://media.edusanjal.com/__sized__/gallery/Winners_of_the_Thames_Inter_College_Cricket_2014-crop-c0-5__0-5-180x120-70.jpg"
    },
    {
      "title": "Thames International College Kathmandu and Webster University, St. Louis",
      "image_url": "https://media.edusanjal.com/__sized__/gallery/Thames_Agreement-crop-c0-5__0-5-180x120-70.jpg"
    },
    {
      "title": "Book Talk 2017 with Rookmangud Katawal",
      "image_url": "https://media.edusanjal.com/__sized__/gallery/Book_Talk_at_Thames-crop-c0-5__0-5-180x120-70.jpg"
    },
    {
      "title": "Thames International College team with students",
      "image_url": "https://media.edusanjal.com/__sized__/gallery/Thames_International_College_One-crop-c0-5__0-5-180x120-70.jpg"
    }
  ],
  "about": "Located in the heart of the city precinct Baneshwor, a cultural melting point of communities from all over the country, Thames International College is a premier academic institution offering a variety of undergraduate programs. The college comprises of three schools, the School of Business and Management, the School of Information Technology, and the School of Social Sciences. \n\nSchool of Social Sciences offers Bachelor of Arts courses which include: \n\nBachelor of Psychology(BPsy), Bachelor of Social Work(BSW), Bachelor of Journalism and Mass Communication(BJM), Bachelor of Rural Development(BRD), Bachelor of Sociology(BSO) \n\nSchool of Information Technology offers: \n\nBachelor of Computer Application (BCA), Bachelor of Information Management (BIM) \n\nSchool of Business and Management currently offers: \n\nBachelor of Business Administration (BBA), Bachelor of Business Management (BBM - Entrepreneurship), Bachelor of Business Management (BBM - Banking Management). The college also offers Bachelor of Business Studies (BBS) and Master of Business Studies (MBS) through the Center for Continuing Education at Thames (CCE). \n\nAll the programs of Thames College lead to a degree from Nepal's oldest and most reputed Tribhuvan University. \n\nThames International College has been accredited and acknowledged with some prestigious academic awards: \n\nTop 10 BBA College of Nepal 2019, 6th Best B-School in Nepal 2014, Best Undergraduate B-School (BIM) 2014, 6th Best B-School in Nepal 2013.",
  "videos": [
    {
      "title": "Edusanjal is a Reliable Platform for Educational Updates in Nepal - Chandan Nayak, Thames College",
      "video_url": "/watch/edusanjal-is-a-reliable-platform-for-educational-updates-in-nepal-chandan-nayak-thames-college/",
      "thumbnail_url": "https://media.edusanjal.com/__sized__/video_thumbnails/edusanjal_is_a_reliable_platform_for_educational_updates_in_nepal_-_chandan_nayak_thames_college-crop-c0-5__0-5-200x112-70.jpg"
    },
    {
      "title": "EduTalk 83 - Importance of Inter-Disciplinary Education and Independent Learning - Thames College",
      "video_url": "/watch/edutalk-83-importance-of-inter-disciplinary-education-and-independent-learning-thames-college/",
      "thumbnail_url": "https://media.edusanjal.com/__sized__/video_thumbnails/edutalk_83_-_importance_of_inter-disciplinary_education_and_independent_learning_-_thames_college-crop-c0-5__0-5-200x112-70.jpg"
    },
    {
      "title": "Exploring the Future of Social Science Education: Insights, Impact, and Inspiration",
      "video_url": "/watch/exploring-the-future-of-social-science-education-insights-impact-and-inspiration/",
      "thumbnail_url": "https://media.edusanjal.com/__sized__/video_thumbnails/exploring_the_future_of_social_science_education_insights_impact_and_inspiration-crop-c0-5__0-5-200x112-70.webp"
    }
  ]
}
```