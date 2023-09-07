import requests
from bs4 import BeautifulSoup


class MITCourse:
    def __init__(self, course_url):
        self.base_url = "https://ocw.mit.edu"
        self.course_url = course_url
        self.course_syllabus_url = f'{self.base_url}/{self.course_url}/pages/syllabus/'
        self._get_prerequisites()

    def _get_prerequisites(self):
        print(self.course_syllabus_url)
        syllabus_content = requests.get(
            self.course_syllabus_url,
            headers={'User-agent': 'Mozilla/5.0'}
        )
        soup = BeautifulSoup(syllabus_content.content, 'html.parser')
        try:
            return [
                elem.attrs['href']
                for elem in soup
                .find('body')
                .find('div')
                .find('article')
                .find('main')
                .find(['h3', 'h4'], attrs={'id': "prerequisites"})
                .find_next('p')
                .find_all('a')
            ]
        except Exception as e:
            print(e)
            return []


if __name__ == "__main__":
    course_url = "courses/18-650-statistics-for-applications-fall-2016"
    MITCourse(course_url)

