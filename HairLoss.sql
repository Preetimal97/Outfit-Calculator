Create Table HairLoss (Id integer, Genetics text, HormonalChanges text,
					    MedicalConditions text, MedicationsTreatments text, NutritionalDeficiencies
					   text, Stress text, Age text, PoorHairCareHabits text,
					   EnvironmentalFactors text, 
					   Smoking text, WeightLoss text, HairLoss 
					   integer);
					   
select * from HairLoss limit 20

/* Shows where HairLoss = 1 as a true statement through boolean */
select * 
from HairLoss
where HairLoss = 1;

/* Changed from boolean type to text type for the column HairLoss */
Alter Table HairLoss
Alter Column Hairloss TYPE text USING Hairloss::text;

/* Changed from 1 (the true boolean) being used to label hairloss to actual text 'True' in its place*/
Update HairLoss
Set Hairloss = 'True'
Where Hairloss = '1';
Select * from HairLoss;

/* Changed from 0 (the false boolean) being used to label hairloss to actual text 'False' in its place*/
Update HairLoss
Set Hairloss = 'False'
Where Hairloss = '0';
Select * from HairLoss;

/* Changed type of age from text to int */
Alter Table HairLoss
Alter Column age TYPE integer USING age::integer;



/* Shows where the person has a high stress level and is above the age of 40*/
select * 
from HairLoss
where stress = 'High'and age > 40;

/* Subquery to show genetics, stress, age, and hairloss where age is less than 30 and genetics isn't there */
select id, genetics, stress, age, Hairloss
from HairLoss
where age < 30 and genetics = 'No';


/* Creates a sub-table from original table HairLoss called HighStress where there are
no genes for hair loss and the subject is under age 30 but are under high stress */
Select * INTO HighStress From HairLoss
Where stress = 'High' and age < 30 and genetics = 'No'



Select *
from HighStress

/* Creates a sub-table from original table HairLoss called LowStress where there are
no genes for hair loss and the subject is under age 30 but are under Low stress */

Select * INTO LowStress From HairLoss
Where stress = 'Low' and age < 30 and genetics = 'No'

Select *
from LowStress

select id, genetics, stress, age, Hairloss
from HighStress

select id, genetics, stress, age, Hairloss
from LowStress


/* Counts where hairloss is evident which is 37 times proving that  high stress
plays a role despite good genes and youth based on this small sample*/
select count (*)
From HighStress
where hairloss = 'True'


/* Counts where hairloss is evident only 22 times proving that low stress
plays a role despite good genes and youth based on this small sample*/
select count (*)
From LowStress
where hairloss = 'True'







