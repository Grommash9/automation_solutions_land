from django.shortcuts import render
from django.views import View
from .models import TeamMember, WorkExample


class LandPage(View):
    def get(self, request):
        team_members = TeamMember.objects.filter()
        for members in team_members:
            members.avatar_b64 = members.avatar_b64.decode('utf-8')

        works_examples = WorkExample.objects.filter()
        for work in works_examples:
            work.avatar_b64 = work.avatar_b64.decode('utf-8')

        return render(request, 'main_page.html', context={'team_members': team_members,
                                                          'works_examples': works_examples})
