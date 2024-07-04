select fifteen.country,
fifteen.Happiness_Rank as "2015",
sixteen.Happiness_Rank as "2016",
seventeen.Happiness_Rank as "2017", 
eighteen.Overall_rank as "2018",
nineteen.Overall_rank as "2019"

from 

[dbo].[2015] fifteen
inner join [dbo].[2016] sixteen
on fifteen.country = sixteen.country
join [dbo].[2017] seventeen
on fifteen.country = seventeen.country
join [dbo].[2018] eighteen
on fifteen.country = eighteen.Country_or_region
join [dbo].[2019] nineteen
on fifteen.country = nineteen.Country_or_region

