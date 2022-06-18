next_page = 'https://www.basketball-reference.com/players/' + 'a' + '/'
if PaginationScraper.page_number < 6:
    PaginationScraper.page_number += 1

    yield response.follow(next_page, callback=self.parse)



