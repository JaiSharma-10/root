create database Analysis;
use Analysis;

select * from [dbo].[MovieData]

create schema stg

alter schema stg transfer [dbo].[MovieData]

select * from stg.MovieData

CREATE TABLE dbo.DbErrors
         (ErrorID        INT IDENTITY(1, 1),
          UserName       VARCHAR(100),
          ErrorNumber    INT,
          ErrorState     INT,
          ErrorSeverity  INT,
          ErrorLine      INT,
          ErrorProcedure VARCHAR(MAX),
          ErrorMessage   VARCHAR(MAX),
          ErrorDateTime  DATETIME)
GO

create schema MovieDataAnalyis

-- DimRating
alter schema MovieDataAnalyis transfer [dbo].[DimRating]

insert into [MovieDataAnalyis].[DimRating] (Rating)
select distinct [Rating]
from [stg].[MovieData]
 
select * from [MovieDataAnalyis].[DimRating]


-- DimYear
alter schema MovieDataAnalyis transfer [dbo].[DimYear]

insert into [MovieDataAnalyis].[DimYear] ([Year])
select distinct [Year]
from [stg].[MovieData]

select * from [MovieDataAnalyis].[DimYear]

-- DimVote
alter schema MovieDataAnalyis transfer [dbo].[DimVote]

insert into [MovieDataAnalyis].[DimVote] ([Vote])
select distinct [Votes]
from [stg].[MovieData]

select * from [MovieDataAnalyis].[DimVote]

-- FctMovieData

ALTER SCHEMA MovieDataAnalyis transfer [dbo].[FctMovieData]

INSERT INTO [MovieDataAnalyis].[FctMovieData] (
		[RatingId],
		[VoteId],
		[YearId],
		[Title],
		[Genre],
		[Description],
		[Director],
		[Actors]
		)

SELECT 
		DR.[RatingId],
		DV.[VoteId],
		DY.[YearId],
		[Title],
		[Genre],
		[Description],
		[Director],
		[Actors]
	
FROM
	[stg].[MovieData] MD
INNER JOIN
	[MovieDataAnalyis].[DimRating]  DR
ON
	MD.[Rating]=DR.[Rating]
INNER JOIN
	[MovieDataAnalyis].[DimVote] DV
ON 
	MD.[Votes]=DV.[Vote]
INNER JOIN
	 [MovieDataAnalyis].[DimYear] DY
ON	
	MD.[Year]=DY.[Year]


Select * from [MovieDataAnalyis].[FctMovieData]