USE [master]
GO
/****** Object:  Database [Educational administration]    Script Date: 2021/6/13 14:07:37 ******/
CREATE DATABASE [Educational administration]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'Educational administration', FILENAME = N'D:\SQL Server2019\MSSQL15.MSSQLSERVER\MSSQL\DATA\Educational administration.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'Educational administration_log', FILENAME = N'D:\SQL Server2019\MSSQL15.MSSQLSERVER\MSSQL\DATA\Educational administration_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [Educational administration] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [Educational administration].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [Educational administration] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [Educational administration] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [Educational administration] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [Educational administration] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [Educational administration] SET ARITHABORT OFF 
GO
ALTER DATABASE [Educational administration] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [Educational administration] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [Educational administration] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [Educational administration] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [Educational administration] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [Educational administration] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [Educational administration] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [Educational administration] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [Educational administration] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [Educational administration] SET  DISABLE_BROKER 
GO
ALTER DATABASE [Educational administration] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [Educational administration] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [Educational administration] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [Educational administration] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [Educational administration] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [Educational administration] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [Educational administration] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [Educational administration] SET RECOVERY FULL 
GO
ALTER DATABASE [Educational administration] SET  MULTI_USER 
GO
ALTER DATABASE [Educational administration] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [Educational administration] SET DB_CHAINING OFF 
GO
ALTER DATABASE [Educational administration] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [Educational administration] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [Educational administration] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [Educational administration] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'Educational administration', N'ON'
GO
ALTER DATABASE [Educational administration] SET QUERY_STORE = OFF
GO
USE [Educational administration]
GO
/****** Object:  Table [dbo].[Course]    Script Date: 2021/6/13 14:07:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Course](
	[COURSEID] [nvarchar](20) NOT NULL,
	[COURSENAME] [nvarchar](20) NOT NULL,
	[CREDIT] [float] NULL,
	[DESCRIPTION] [nvarchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[COURSEID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Grades]    Script Date: 2021/6/13 14:07:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Grades](
	[JXBID] [nvarchar](20) NOT NULL,
	[USERID] [nvarchar](20) NOT NULL,
	[SCORE] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[JXBID] ASC,
	[USERID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[JXB]    Script Date: 2021/6/13 14:07:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[JXB](
	[JXBID] [nvarchar](20) NOT NULL,
	[COURSEID] [nvarchar](20) NOT NULL,
	[USERID] [nvarchar](20) NOT NULL,
	[DESCRIPTION] [nvarchar](100) NULL,
PRIMARY KEY CLUSTERED 
(
	[JXBID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[UserInfo]    Script Date: 2021/6/13 14:07:38 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[UserInfo](
	[USERID] [nvarchar](20) NOT NULL,
	[USERNAME] [nvarchar](20) NOT NULL,
	[GENDER] [nvarchar](2) NULL,
	[BIRTHDAY] [nvarchar](11) NULL,
	[DEPARTMENT] [nvarchar](50) NULL,
	[PHONE] [nvarchar](20) NULL,
	[USERTYPE] [nvarchar](4) NULL,
	[PASSWORD] [nvarchar](20) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[USERID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
USE [master]
GO
ALTER DATABASE [Educational administration] SET  READ_WRITE 
GO
