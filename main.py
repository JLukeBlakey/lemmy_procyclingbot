from os import environ
from time import gmtime, strftime

from plemmy import LemmyHttp
from plemmy.responses import GetCommunityResponse

from procyclingstats import Race


year='2023'
current_date=strftime('%m-%d',gmtime())

procyclingstats_url='https://www.procyclingstats.com'

vuelta_url='https://www.lavuelta.es/en'
vuelta_profile_url='https://cdn.cyclingstage.com/images/vuelta-spain/' + year # full e.g. https://cdn.cyclingstage.com/images/vuelta-spain/2023/stage-7-profile.jpg

instance='https://lemmy.world'
community='procycling'
user='procyclingbot'
password=environ['LEMMY_PROCYCLINGBOT_PASSWORD']

lemmy_instance = LemmyHttp(instance)
lemmy_instance.login(user, password)

api_response_get_community = lemmy_instance.get_community(name=community)
community = GetCommunityResponse(api_response_get_community).community_view.community

vuelta=Race("race/vuelta-a-espana/" + year)

for stage in vuelta.stages():
    if stage['date'] == current_date:
        stage_number=str(stage['stage_name'].split()[1])
        title=year + ' ' + vuelta.name() + ' - Stage ' + stage_number
        body=f'![Stage Profile]({vuelta_profile_url}/stage-{stage_number}-profile.jpg)\n\n' + \
             stage['stage_name'] + ' | ' + f'[Tracking & Results]({procyclingstats_url}/{stage["stage_url"]})'
        url=vuelta_url + '/stage-' + stage_number
        api_response_create_post = lemmy_instance.create_post(community.id, title, body, url=url)
