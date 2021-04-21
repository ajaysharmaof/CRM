from django.shortcuts import render, redirect, reverse
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


#CRUD+L - create, retrive ,update, delete, + listview

class LandingPageView(TemplateView):
    template_name = "landing.html"

def landing_page(request):
    return render(request, "landing.html")



class LeadListView(ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"    #by default context variable like lead is object_list or u can change

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request,"leads/lead_list.html",context)



class LeadDetailView(DetailView):
    template_name = "leads/lead_detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"

def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)



class LeadCreateView(CreateView):
    template_name = "leads/lead_create.html"
    form_class = LeadModelForm
    
    def get_success_url(self):
        return reverse("leads:lead-list")
        
def lead_create(request):
    form = LeadModelForm()
    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request,"leads/lead_create.html", context)



class LeadUpdateView(UpdateView):
    template_name = "leads/lead_update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead-list")

def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)   #an instance single instance of model to want to update 
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, "leads/lead_update.html", context)

    

class LeadDeleteView(DeleteView):
    template_name = "leads/lead_delete.html"
    queryset = Lead.objects.all()

    def get_success_url(self):
        return reverse("leads:lead-list")

def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")


""" 
def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)  #grab the object
    form = LeadForm()   #instiate form object
    if request.method == "POST":
        form = LeadForm(request.POST) #pass the data in form
        #print("Receiving a post request")
        if form.is_valid():
            #print("The Form is valid")
            #print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            age        = form.cleaned_data['age']
            
            #update the data
            lead.first_name = first_name
            lead.last_name  = last_name
            lead.age        = age
            lead.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }

    return render(request,"leads/lead_update.html", context)
 """
""" 
def lead_create(request):
    form = LeadModelForm()   #instiate form object
    if request.method == "POST":
        form = LeadModelForm(request.POST) #pass the data in form
        #print("Receiving a post request")
        if form.is_valid():
            #print("The Form is valid")
            #print(form.cleaned_data)
            first_name = form.cleaned_data['first_name']
            last_name  = form.cleaned_data['last_name']
            age        = form.cleaned_data['age']
            agent      = Agent.objects.first()  #grab first row of sql table 
            Lead.objects.create(        #onject manager
                first_name = first_name,
                last_name  = last_name,
                age        = age,
                agent      = agent,
            )
            return redirect("/leads")
    context = {
        "form": form
    }
    return render(request,"leads/lead_create.html", context)
     """