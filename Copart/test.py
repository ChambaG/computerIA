url = """<li class="auction-yard-loctaion" ng-repeat="auction in auctionsByDay.auction | orderBy:'saleName'"><!-- --><a brand"COPART" data-url="/saleListResult/131/2018-11-26?location=FL - Jacksonville East&amp;saleDate=1543244400000&amp;liveAuction=false&amp;from=&amp;yardNum=131" href="./saleListResult/131/2018-11-26?location=FL - Jacksonville East&amp;saleDate=1543244400000&amp;liveAuction=false&amp;from=&amp;yardNum=131" ng-if="auction.yardNumber!=0 &amp;&amp;"""

print(url.find("data-url"))
print(url[url.find("data-url")])