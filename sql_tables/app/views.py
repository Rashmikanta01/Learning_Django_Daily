from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import Prefetch

def emptodeptjoin(request):
    # QLEDO=EMP.objects.all().select_related('DEPTNO')
    # #QLEDO=EMP.objects.all().select_related('DEPTNO').filter(DEPTNO__DNAME='Accounting')
    # QLEDO=EMP.objects.all().select_related('DEPTNO').filter(ENAME__startswith='R')
    # QLEDO=EMP.objects.all().select_related('DEPTNO').filter(DEPTNO__LOC='newyork')
    # QLEDO=EMP.objects.all().select_related('DEPTNO').filter(JOB='president',DEPTNO__DNAME='Accounting')
    # QLEDO=EMP.objects.all().select_related('DEPTNO').filter(ENAME='Deeps')
    # QLEDO=EMP.objects.select_related('DEPTNO').filter(DEPTNO__DNAME='Accounting')
    # QLEDO=EMP.objects.select_related('DEPTNO').filter(DEPTNO__DNAME='Accounting',ENAME__startswith='R')
    # QLEDO=EMP.objects.select_related('DEPTNO').filter(SAL__gt=200)
    # QLEDO=EMP.objects.select_related('DEPTNO').filter(SAL__gt=200,DEPTNO__DNAME='Accounting')
    # QLEDO=EMP.objects.select_related('DEPTNO').filter(ENAME='Deeps',DEPTNO__DNAME='Accounting')
    # QLEDO=EMP.objects.select_related('DEPTNO').filter(DEPTNO__DNAME='operations')
    # QLEDO=EMP.objects.select_related('DEPTNO').filter(DEPTNO__DNAME='management')
    # QLEDO=EMP.objects.select_related('DEPTNO').filter(DEPTNO__DNAME='Accounting',ENAME='Subhs')
    # QLEDO=EMP.objects.select_related('DEPTNO').filter(DEPTNO__DNAME='operations',ENAME='Biswa', SAL__gt=200)


    QLEDO=EMP.objects.all().select_related('DEPTNO')

    QLEMO=EMP.objects.all().select_related('MGR').filter(ENAME='Deeps')
    QLEMO=EMP.objects.all().select_related('MGR').filter(MGR__ENAME='Subhs')
    QLEMO=EMP.objects.all().select_related('MGR').filter(MGR__ENAME='Subhs',SAL__gt=200)
    QLEMO=EMP.objects.all().select_related('MGR').filter(MGR__ENAME='Subhs',DEPTNO__DNAME='management')
    QLEMO=EMP.objects.all().select_related('MGR').filter(MGR__ENAME='Subhs',DEPTNO__DNAME='management',JOB='Analyst')
    QLEMO=EMP.objects.all().select_related('MGR').filter(MGR__ENAME='Subhs',DEPTNO__DNAME='management',JOB='Analyst',SAL__gt=200)
    QLEMO=EMP.objects.all().select_related('MGR').filter(MGR__ENAME='Subhs',DEPTNO__DNAME='management',JOB='Analyst',SAL__gt=200,ENAME='Ranjan')
    QLEMO=EMP.objects.all().select_related('MGR').filter(SAL__gt=200)
    QLEMO=EMP.objects.all().select_related('MGR').filter(SAL__gt=200,MGR__ENAME='Subhs')
    QLEMO=EMP.objects.all().select_related('MGR').filter(DEPTNO__DNAME='management')
    QLEMO=EMP.objects.all().select_related('MGR').filter(DEPTNO__DNAME='management',MGR__ENAME='Subhs')
    QLEMO=EMP.objects.all().select_related('MGR').filter(DEPTNO__DNAME='Accounting')
    QLEMO=EMP.objects.all().select_related('MGR').filter(DEPTNO__DNAME='operations')
    QLEMO=EMP.objects.all().select_related('MGR').filter(DEPTNO__DNAME='operations',MGR__ENAME='Biswa')
    QLEMO=EMP.objects.all().select_related('MGR').filter(DEPTNO__DNAME='operations',ENAME='Sushma')



    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR')
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(DEPTNO__DNAME='Accounting',MGR__ENAME='Subhs')
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(DEPTNO__DNAME='Accounting',MGR__ENAME='Subhs',SAL__gt=200)
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(DEPTNO__DNAME='management',MGR__ENAME='Subhs',JOB='Analyst')
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(DEPTNO__DNAME='operations',MGR__ENAME='Biswa',ENAME='Sushma')
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(SAL__gt=200)
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(DEPTNO__DNAME='management')
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(DEPTNO__DNAME='operations')
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(DEPTNO__DNAME='Accounting')
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(MGR__ENAME='Subhs')
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(MGR__ENAME='Biswa')
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(ENAME='Deeps')
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(ENAME='Sushma')
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(ENAME='Ranjan')
    QLEDMO=EMP.objects.all().select_related('DEPTNO','MGR').filter(ENAME='Biswa')
    
    d={'QLEDO': QLEDO ,
        'QLEMO':QLEMO,
        'QLEDMO':QLEDMO}
    return render(request,'emptodeptjoin.html' ,d)

def depttoemp_pfr(request):
    QLDEO= DEPT.objects.all().prefetch_related('emp_set').filter(DNAME='Accounting')
    #QLDEO=DEPT.objects.all().prefetch_related('emp_set').filter(DNAME='Accounting')
    #QLDEO=DEPT.objects.prefetch_related(Prefetch('emp_set',queryset=EMP.objects.filter(ENAME='Deeps')))
    QLDEO=DEPT.objects.prefetch_related(Prefetch('emp_set',queryset=EMP.objects.filter(ENAME='Biswa')| EMP.objects.filter(DEPTNO__DNAME='Accounting')))
    
    QLDEO=DEPT.objects.prefetch_related('emp_set').filter(DETPNO='Accounting')

    d={'QLDEO':QLDEO}
    return render(request,'depttoemp_pfr.html',d)




