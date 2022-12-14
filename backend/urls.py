
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("calendar", Calendar, name="calendar"),
    path("chartd", ChartD, name="chartd"),
    path("chartchartist", ChartChartist, name="chartchartist"),
    path("chartchartjs", ChartChartjs, name="chartchartjs"),
    path("chartdynamic", ChartDynamic, name="chartdynamic"),
    path("chartflot", ChartFlot, name="chartflot"),
    path("chartknob", ChartKnob, name="chartknob"),
    path("chartmorris", ChartMorris, name="chartmorris"),
    path("chartother", ChartOther, name="chartother"),
    path("chartsparkline", ChartSparkline, name="chartsparkline"),
    path("compose", Compose, name="compose"),
    path("dashboard", Dashboard, name="dashboard"),
    path("emailtemplateverify", EmailTemplateVerify, name="emailtemplateverify"),
    path("extrascontact", ExtrasContact, name="extrascontact"),
    path("extrasemailtemplate", ExtrasEmailTemplate, name="extrasemailtemplate"),
    path("extrasfaq", ExtrasFaq, name="extrasfaq"),
    path("extrasgallery", ExtrasGallery, name="extrasgallery"),
    path("extrasinvoice", ExtrasInvoice, name="extrasinvoice"),
    path("extrasmaps", ExtrasMaps, name="extrasmaps"),
    path("extraspricing", ExtrasPricing, name="extraspricing"),
    path("extrasprojects", ExtrasProjects, name="extrasprojects"),
    path("extrastaskboard", ExtrasTaskboard, name="extrastaskboard"),
    path("extrastimeline", ExtrasTimeline, name="extrastimeline"),
    path("extrastour", ExtrasTour, name="extrastour"),
    path("formadvanced", FormAdvanced, name="formadvanced"),
    path("formelements", FormElements, name="formelements"),
    path("formfileupload", FormFileupload, name="formfileupload"),
    path("formvalidation", FormValidation, name="formvalidation"),
    path("formwizard", FormWizard, name="formwizard"),
    path("formwysiwig", FormWysiwig, name="formwysiwig"),
    path("formxeditable", FormXeditable, name="formxeditable"),
    path("iconsfontawesomeicons", IconsFontAwesomeIcons, name="iconsfontawesomeicons"),
    path("iconsfontello", IconsFontello, name="iconsfontello"),
    path("iconsmaterialdesigniconic", IconsMaterialDesignIconic, name="iconsmaterialdesigniconic"),
    path("iconsmaterialicons", IconsMaterialIcons, name="iconsmaterialicons"),
    path("iconsthemifyicons", IconsThemifyIcons, name="iconsthemifyicons"),
    path("inbox", Inbox, name="inbox"),
    path("index", Index, name="index"),
    path("page404", Page404, name="page404"),
    path("page500", Page500, name="page500"),
    path("pageconfirmmail", PageConfirmMail, name="pageconfirmmail"),
    path("pagelockscreen", PageLockScreen, name="pagelockscreen"),
    path("pagelogin", PageLogin, name="pagelogin"),
    path("pagerecoverpw", PageRecoverpw, name="pagerecoverpw"),
    path("pageregister", PageRegister, name="pageregister"),
    path("pagestarter", PageStarter, name="pagestarter"),
    path("profile", Profile, name="profile"),
    path("readmail", ReadMail, name="readmail"),
    path("tablesbasic", TablesBasic, name="tablesbasic"),
    path("tablesdatatable", TablesDatatable, name="tablesdatatable"),
    path("tableseditable", TablesEditable, name="tableseditable"),
    path("tablesresponsive", TablesResponsive, name="tablesresponsive"),
    path("uibuttons", UiButtons, name="uibuttons"),
    path("uicards", UiCards, name="uicards"),
    path("uicheckboxradio", UiCheckboxRadio, name="uicheckboxradio"),
    path("uicomponents", UiComponents, name="uicomponents"),
    path("uidraggablecards", UiDraggableCards, name="uidraggablecards"),
    path("uimodals", UiModals, name="uimodals"),
    path("uinotification", UiNotification, name="uinotification"),
    path("uirangeslider", UiRangeSlider, name="uirangeslider"),
    path("uisweetalert", UiSweetalert, name="uisweetalert"),
    path("uitreeview", UiTreeview, name="uitreeview"),
    path("uitypography", UiTypography, name="uitypography"),
    path("widgets", Widgets, name="widgets"),


]   