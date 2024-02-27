import scrapy

class RedditSpider(scrapy.Spider):
    name = 'reddit'
    allowed_domains = ['old.reddit.com']
    start_urls = ['https://old.reddit.com/r/explainlikeimfive/']
    post_count = 0  # Add this line to keep track of the number of posts scraped.

    def parse(self, response):
        for post in response.css('div.thing'):
            if self.post_count < 100:  # Check if less than 100 posts have been scraped.
                yield {
                    'title': post.css('p.title a::text').get(),
                    'poster': post.css('a.author::text').get(),
                    'time': post.css('time::attr(title)').get(),
                    'subreddit': response.url.split('/')[4],
                    'url': post.css('p.title a::attr(href)').get()
                }
                self.post_count += 1  # Increment the count for each post scraped.
            else:
                break  # Stop the loop after 100 posts.

        # Go on to the next page only if less than 100 posts have been scraped.   
        if self.post_count < 100:
            next_page = response.css('span.next-button a::attr(href)').get()
            if next_page:
                yield response.follow(next_page, self.parse)