from django.shortcuts import render

# Create your views here.

# pages/views.py
# pages/views.py
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse


def homePost(request):
    # Use request object to extract choice.

    iqScore = -999
    communication_skills = -999
    projectManagementExperience = -999
    programmingProfiency = -999
    leadershipAbility = -999
    technicalKnowldge = -999
    creativityScore = -999
    analyticalSkills = -999
    teamworkSkills = -999
    problemSolvingAbility = -999

    try:
        # Extract value from request object by control name.
        iqScore = request.POST['iq_score']
        communicationSkill = request.POST['communication_skills']
        projectManagementExperience = request.POST['project_management_experience']
        programmingProfiency = request.POST['programming_proficiency']
        leadershipAbility = request.POST['leadership_ability']
        technicalKnowldge = request.POST['technical_knowledge']
        creativityScore = request.POST['creativity_score']
        analyticalSkills = request.POST['analytical_skills']
        teamworkAbility = request.POST['teamwork_ability']
        problemSolvingAbility = request.POST['problem_solving_ability']

        # Crude debugging effort.
        iqScore = int(iqScore)
        communicationSkill = int(communicationSkill)
        projectManagementExperience = int(projectManagementExperience)
        programmingProfiency = int(programmingProfiency)
        leadershipAbility = int(leadershipAbility)
        technicalKnowldge = int(technicalKnowldge)
        creativityScore = int(creativityScore)
        analyticalSkills = int(analyticalSkills)
        teamworkAbility = int(teamworkAbility)
        problemSolvingAbility = int(problemSolvingAbility)

    # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'home.html', {
            'errorMessage': '*** The data submitted is invalid. Please try again.', })
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', kwargs={'iqScore': iqScore,
                                                               'communicationSkill': communicationSkill,
                                                               'projectManagementExperience': projectManagementExperience,
                                                               'programmingProfiency': programmingProfiency,
                                                               'leadershipAbility': leadershipAbility,
                                                               'technicalKnowldge': technicalKnowldge,
                                                               'creativityScore': creativityScore,
                                                               'analyticalSkills': analyticalSkills,
                                                               'teamworkAbility': teamworkAbility,
                                                               'problemSolvingAbility': problemSolvingAbility}, ))


import pickle
import pandas as pd


def results(request, iqScore, communicationSkill, projectManagementExperience, programmingProfiency,
            leadershipAbility, technicalKnowldge, creativityScore, analyticalSkills, teamworkAbility,
            problemSolvingAbility):
    print("*** Inside reults()")
    # load saved model
    with open('logistic_model.pkl', 'rb') as f:
        loadedModel = pickle.load(f)

    # singleSampleDf = pd.DataFrame(
    #     columns=['iq_score', 'communication_skills', 'project_management_experience', 'programming_proficiency',
    #              'leadership_ability', 'technical_knowledge', 'creativity_score', 'analytical_skills', 'teamwork_ability',
    #              'problem_solving_ability'])

    singleSampleDf = pd.DataFrame(
        columns=['iq_score', 'project_management_experience', 'problem_solving_ability'])

    print("*** IQ Score: " + str(iqScore))
    print("*** Communication Skill: " + str(communicationSkill))
    print("*** Project Management Experience: " + str(projectManagementExperience))
    print("*** Programming Proficiency: " + str(programmingProfiency))
    print("*** Leadership Ability: " + str(leadershipAbility))
    print("*** Technical Knowledge: " + str(technicalKnowldge))
    print("*** Creativity Score: " + str(creativityScore))
    print("*** Analytical Skills: " + str(analyticalSkills))
    print("*** Teamwork Ability: " + str(teamworkAbility))
    print("*** Problem Solving Ability: " + str(problemSolvingAbility))

    # singleSampleDf = singleSampleDf._append({'iq_score': iqScore,
    #                                          'communication_skills': communicationSkill,
    #                                          'project_management_experience': projectManagementExperience,
    #                                          'programming_proficiency': programmingProfiency,
    #                                          'leadership_ability': leadershipAbility,
    #                                          'technical_knowledge': technicalKnowldge,
    #                                          'creativity_score': creativityScore,
    #                                          'analytical_skills': analyticalSkills,
    #                                          'teamwork_ability': teamworkAbility,
    #                                          'problem_solving_ability': problemSolvingAbility},
    #                                         ignore_index=True)

    singleSampleDf = singleSampleDf._append({'iq_score': iqScore,
                                             'project_management_experience': projectManagementExperience,
                                             'problem_solving_ability': problemSolvingAbility},
                                            ignore_index=True)

    singlePrediction = loadedModel.predict(singleSampleDf)

    singlePrediction = "Job Offer" if singlePrediction[0] == 1 else "No Job Offer"

    print("Single prediction: " + str(singlePrediction))

    return render(request, 'results.html', {
        'prediction': singlePrediction, 'iqScore': iqScore,
        'communicationSkill': communicationSkill,
        'projectManagementExperience': projectManagementExperience,
        'programmingProfiency': programmingProfiency,
        'leadershipAbility': leadershipAbility,
        'technicalKnowldge': technicalKnowldge, 'creativityScore': creativityScore,
        'analyticalSkills': analyticalSkills, 'teamworkAbility': teamworkAbility,
        'problemSolvingAbility': problemSolvingAbility})


def homePageView(request):
    # Generate range for communication skills
    selection_range = range(6)

    # return request object and specify page.
    return render(request, 'home.html', {
        'mynumbers': [1, 2, 3, 4, 5, 6, ],
        'firstName': 'Amadeus',
        'lastName': 'Min',
        'selection_range': selection_range,
    })


def aboutPageView(request):
    # return request object and specify page.
    return render(request, 'about.html')


def firstNamePageView(request):
    return render(request, 'amadeus.html')
