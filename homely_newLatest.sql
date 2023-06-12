-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 16, 2021 at 10:21 AM
-- Server version: 10.3.15-MariaDB
-- PHP Version: 7.3.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `homely_new`
--

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add faq', 7, 'add_faq'),
(26, 'Can change faq', 7, 'change_faq'),
(27, 'Can delete faq', 7, 'delete_faq'),
(28, 'Can view faq', 7, 'view_faq'),
(29, 'Can add property', 8, 'add_property'),
(30, 'Can change property', 8, 'change_property'),
(31, 'Can delete property', 8, 'delete_property'),
(32, 'Can view property', 8, 'view_property'),
(33, 'Can add testimonials', 9, 'add_testimonials'),
(34, 'Can change testimonials', 9, 'change_testimonials'),
(35, 'Can delete testimonials', 9, 'delete_testimonials'),
(36, 'Can view testimonials', 9, 'view_testimonials'),
(37, 'Can add comment', 10, 'add_comment'),
(38, 'Can change comment', 10, 'change_comment'),
(39, 'Can delete comment', 10, 'delete_comment'),
(40, 'Can view comment', 10, 'view_comment'),
(41, 'Can add document', 11, 'add_document'),
(42, 'Can change document', 11, 'change_document'),
(43, 'Can delete document', 11, 'delete_document'),
(44, 'Can view document', 11, 'view_document'),
(45, 'Can add sponsor', 12, 'add_sponsor'),
(46, 'Can change sponsor', 12, 'change_sponsor'),
(47, 'Can delete sponsor', 12, 'delete_sponsor'),
(48, 'Can view sponsor', 12, 'view_sponsor'),
(49, 'Can add financial modal', 13, 'add_financialmodal'),
(50, 'Can change financial modal', 13, 'change_financialmodal'),
(51, 'Can delete financial modal', 13, 'delete_financialmodal'),
(52, 'Can view financial modal', 13, 'view_financialmodal'),
(53, 'Can add association', 14, 'add_association'),
(54, 'Can change association', 14, 'change_association'),
(55, 'Can delete association', 14, 'delete_association'),
(56, 'Can view association', 14, 'view_association'),
(57, 'Can add code', 15, 'add_code'),
(58, 'Can change code', 15, 'change_code'),
(59, 'Can delete code', 15, 'delete_code'),
(60, 'Can view code', 15, 'view_code'),
(61, 'Can add nonce', 16, 'add_nonce'),
(62, 'Can change nonce', 16, 'change_nonce'),
(63, 'Can delete nonce', 16, 'delete_nonce'),
(64, 'Can view nonce', 16, 'view_nonce'),
(65, 'Can add user social auth', 17, 'add_usersocialauth'),
(66, 'Can change user social auth', 17, 'change_usersocialauth'),
(67, 'Can delete user social auth', 17, 'delete_usersocialauth'),
(68, 'Can view user social auth', 17, 'view_usersocialauth'),
(69, 'Can add partial', 18, 'add_partial'),
(70, 'Can change partial', 18, 'change_partial'),
(71, 'Can delete partial', 18, 'delete_partial'),
(72, 'Can view partial', 18, 'view_partial'),
(73, 'Can add profile', 19, 'add_profile'),
(74, 'Can change profile', 19, 'change_profile'),
(75, 'Can delete profile', 19, 'delete_profile'),
(76, 'Can view profile', 19, 'view_profile'),
(77, 'Can add profile_ finance', 20, 'add_profile_finance'),
(78, 'Can change profile_ finance', 20, 'change_profile_finance'),
(79, 'Can delete profile_ finance', 20, 'delete_profile_finance'),
(80, 'Can view profile_ finance', 20, 'view_profile_finance'),
(81, 'Can add profile finance', 20, 'add_profilefinance'),
(82, 'Can change profile finance', 20, 'change_profilefinance'),
(83, 'Can delete profile finance', 20, 'delete_profilefinance'),
(84, 'Can view profile finance', 20, 'view_profilefinance'),
(85, 'Can add prospectus document', 21, 'add_prospectusdocument'),
(86, 'Can change prospectus document', 21, 'change_prospectusdocument'),
(87, 'Can delete prospectus document', 21, 'delete_prospectusdocument'),
(88, 'Can view prospectus document', 21, 'view_prospectusdocument'),
(89, 'Can add individual kyc', 22, 'add_individualkyc'),
(90, 'Can change individual kyc', 22, 'change_individualkyc'),
(91, 'Can delete individual kyc', 22, 'delete_individualkyc'),
(92, 'Can view individual kyc', 22, 'view_individualkyc'),
(93, 'Can add company kyc', 23, 'add_companykyc'),
(94, 'Can change company kyc', 23, 'change_companykyc'),
(95, 'Can delete company kyc', 23, 'delete_companykyc'),
(96, 'Can view company kyc', 23, 'view_companykyc'),
(97, 'Can add process flow', 24, 'add_processflow'),
(98, 'Can change process flow', 24, 'change_processflow'),
(99, 'Can delete process flow', 24, 'delete_processflow'),
(100, 'Can view process flow', 24, 'view_processflow');

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$216000$ZPV63dF42Sm3$V0jATsXG0fySozShqOdytD6Yh5InakHACxspOQPM4n4=', '2021-02-25 19:39:49.708936', 1, 'jal', 'Jal', 'Singh', 'jlsingh38@gmail.com', 1, 1, '2021-01-28 03:21:57.250362'),
(9, '!qvQcUZk2MQWIHa9wrcoAYlrKZAPq7rPmYD1H2QQW', '2021-02-17 13:05:25.600758', 0, 'jlsingh38', 'Jal', 'Singh', 'jlsingh38@gmail.com', 0, 1, '2021-02-17 13:05:24.217755'),
(16, 'pbkdf2_sha256$216000$kJ6D20U0PaOU$UUQY0EksMAycU9GNj2g8HWIFM4VEAiQ8nOMl7BBBJww=', '2021-02-22 07:57:56.643453', 0, 'Jal2', '', '', '', 0, 1, '2021-02-22 07:57:56.132028'),
(17, 'pbkdf2_sha256$216000$dcmVDCOaN4aR$pRDyt53VkjP9t/yCj2ui6iEADm1PfNWHPnmJzZHmA2M=', '2021-02-22 08:03:18.016967', 0, 'Jal3', '', '', '', 0, 1, '2021-02-22 08:03:17.308213'),
(18, 'pbkdf2_sha256$216000$vUmYouiDhONq$PN/nGj82QntNGwG5uUY9DWeSSSHh5DcLZ2f1WdP5cfc=', '2021-02-25 16:32:53.507129', 0, 'Jal4', '', '', '', 0, 1, '2021-02-25 16:32:52.091896'),
(19, 'pbkdf2_sha256$216000$hIlqxZIlsGLV$k2IpJUWGCLrR8BPFHqsSEUY0LXQdGPos5pAwD776wF0=', '2021-02-25 17:05:45.996561', 0, 'Jal5', '', '', '', 0, 1, '2021-02-25 17:05:44.706882');

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2021-01-28 13:30:57.301608', '1', 'Property one', 1, '[{\"added\": {}}]', 8, 1),
(2, '2021-01-28 13:49:03.060026', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image\"]}}]', 8, 1),
(3, '2021-01-28 16:44:36.459221', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image\", \"Featured image2\", \"Featured image3\"]}}]', 8, 1),
(4, '2021-01-28 16:59:08.535743', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image\", \"Featured image2\"]}}]', 8, 1),
(5, '2021-01-28 17:24:59.682294', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image\", \"Featured image2\", \"Featured image3\"]}}]', 8, 1),
(6, '2021-01-28 17:41:44.759354', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image2\", \"Featured image3\"]}}]', 8, 1),
(7, '2021-01-28 17:50:22.974048', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image2\", \"Featured image3\"]}}]', 8, 1),
(8, '2021-01-28 17:56:09.903308', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image\", \"Featured image4\"]}}]', 8, 1),
(9, '2021-01-28 18:05:27.530198', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image5\"]}}]', 8, 1),
(10, '2021-01-28 18:34:20.079526', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"About builder\", \"Financial\", \"Due diligence\", \"Property details\", \"Updates\", \"Location\", \"Map location\", \"Location detail\", \"Localty\", \"Parking ratio\", \"Floor efficiency\", \"Fit outs\", \"Total area\", \"Power area\", \"Power backup\", \"Area of sale\", \"Air conditioning\", \"Purchase price\", \"Stamp duty\", \"Brokerage\", \"Reserves\", \"Highlights\"]}}]', 8, 1),
(11, '2021-01-28 18:52:21.189222', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Financial desclaimer\"]}}]', 8, 1),
(12, '2021-01-29 10:01:17.408087', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image\"]}}]', 8, 1),
(13, '2021-01-30 05:01:06.485044', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Acquisition\", \"Acquisition frequency\", \"Asset management\", \"Asset management frequency\"]}}]', 8, 1),
(14, '2021-01-30 05:34:58.845962', '1', 'FinancialModal object (1)', 1, '[{\"added\": {}}]', 13, 1),
(15, '2021-01-30 05:35:35.901378', '2', 'FinancialModal object (2)', 1, '[{\"added\": {}}]', 13, 1),
(16, '2021-01-30 05:36:34.192558', '3', 'FinancialModal object (3)', 1, '[{\"added\": {}}]', 13, 1),
(17, '2021-01-30 09:58:24.462811', '1', 'Testimonials object (1)', 1, '[{\"added\": {}}]', 9, 1),
(18, '2021-01-30 10:04:10.121176', '2', 'Testimonials object (2)', 1, '[{\"added\": {}}]', 9, 1),
(19, '2021-01-30 10:04:32.658217', '1', 'Testimonials object (1)', 2, '[{\"changed\": {\"fields\": [\"Image\"]}}]', 9, 1),
(20, '2021-01-30 10:06:23.106256', '1', 'Testimonials object (1)', 2, '[{\"changed\": {\"fields\": [\"Comments\"]}}]', 9, 1),
(21, '2021-01-31 03:21:30.746362', '1', 'Sponsor object (1)', 1, '[{\"added\": {}}]', 12, 1),
(22, '2021-01-31 03:46:20.986074', '1', 'Sponsor object (1)', 2, '[{\"changed\": {\"fields\": [\"Logo\"]}}]', 12, 1),
(23, '2021-01-31 04:05:54.370108', '1', 'Document object (1)', 1, '[{\"added\": {}}]', 11, 1),
(24, '2021-01-31 04:06:15.410632', '2', 'Document object (2)', 1, '[{\"added\": {}}]', 11, 1),
(25, '2021-01-31 04:33:18.250656', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Expected irr\", \"Asset risk\", \"Expected holding period\", \"Minimum investment\", \"Funded member\", \"Total deal size\", \"Total sft\", \"Asset type\"]}}]', 8, 1),
(26, '2021-02-04 10:15:23.024498', '1', 'Faq object (1)', 1, '[{\"added\": {}}]', 7, 1),
(27, '2021-02-04 10:15:30.676092', '2', 'Faq object (2)', 1, '[{\"added\": {}}]', 7, 1),
(28, '2021-02-04 10:15:38.592915', '3', 'Faq object (3)', 1, '[{\"added\": {}}]', 7, 1),
(29, '2021-02-07 13:11:28.812047', '1', 'Profile object (1)', 1, '[{\"added\": {}}]', 19, 1),
(30, '2021-02-07 13:46:58.084877', '1', 'Profile object (1)', 2, '[{\"changed\": {\"fields\": [\"Doc proof\"]}}]', 19, 1),
(31, '2021-02-07 15:22:50.946878', '1', 'Profile object (1)', 2, '[{\"changed\": {\"fields\": [\"Doc proof\"]}}]', 19, 1),
(32, '2021-02-07 16:58:14.815513', '1', 'Profile object (1)', 2, '[{\"changed\": {\"fields\": [\"Doc proof\"]}}]', 19, 1),
(33, '2021-02-08 06:44:10.268503', '1', 'ProfileFinance object (1)', 1, '[{\"added\": {}}]', 20, 1),
(34, '2021-02-11 04:11:47.927936', '1', 'ProspectusDocument object (1)', 1, '[{\"added\": {}}]', 21, 1),
(35, '2021-02-11 04:12:05.872058', '2', 'ProspectusDocument object (2)', 1, '[{\"added\": {}}]', 21, 1),
(36, '2021-02-12 07:38:25.736451', '1', 'individualKyc object (1)', 2, '[{\"changed\": {\"fields\": [\"Id proof\"]}}]', 22, 1),
(37, '2021-02-12 07:41:28.596130', '3', 'individualKyc object (3)', 2, '[{\"changed\": {\"fields\": [\"Id proof\"]}}]', 22, 1),
(38, '2021-02-12 07:45:59.864483', '3', 'individualKyc object (3)', 2, '[]', 22, 1),
(39, '2021-02-12 08:01:35.284968', '5', 'individualKyc object (5)', 3, '', 22, 1),
(40, '2021-02-12 08:01:35.416648', '4', 'individualKyc object (4)', 3, '', 22, 1),
(41, '2021-02-12 08:01:35.438592', '3', 'individualKyc object (3)', 3, '', 22, 1),
(42, '2021-02-12 08:01:35.483437', '2', 'individualKyc object (2)', 3, '', 22, 1),
(43, '2021-02-12 08:01:35.505378', '1', 'individualKyc object (1)', 3, '', 22, 1),
(44, '2021-02-13 04:27:33.585652', '4', 'JalSingh', 3, '', 4, 1),
(45, '2021-02-13 04:27:33.668920', '2', 'Jal_test', 3, '', 4, 1),
(46, '2021-02-13 04:27:33.813543', '3', 'Jal_test2', 3, '', 4, 1),
(47, '2021-02-13 08:21:07.055518', '5', 'JalSingh', 3, '', 4, 1),
(48, '2021-02-17 12:54:49.912785', '8', 'jal8426dd03919b484f', 3, '', 4, 1),
(49, '2021-02-17 12:54:50.059760', '7', 'JalSingh', 3, '', 4, 1),
(50, '2021-02-17 12:54:50.257411', '6', 'jlsingh38', 3, '', 4, 1),
(51, '2021-02-18 04:42:58.299474', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image\", \"Featured image2\", \"Featured image3\", \"Featured image4\", \"Featured image5\", \"Featured image6\", \"Featured image7\", \"Featured image8\", \"Featured image9\", \"Featured image10\"]}}]', 8, 1),
(52, '2021-02-18 04:46:54.800515', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image\", \"Featured image2\", \"Featured image3\", \"Featured image4\", \"Featured image5\", \"Featured image6\", \"Featured image7\", \"Featured image8\", \"Featured image9\", \"Featured image10\"]}}]', 8, 1),
(53, '2021-02-18 04:47:50.381016', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image6\"]}}]', 8, 1),
(54, '2021-02-18 04:48:31.192065', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image5\"]}}]', 8, 1),
(55, '2021-02-18 04:49:44.930458', '1', 'Property one', 2, '[{\"changed\": {\"fields\": [\"Featured image7\", \"Featured image10\"]}}]', 8, 1),
(56, '2021-02-21 05:11:35.830851', '2', 'The Pavilion III', 1, '[{\"added\": {}}]', 8, 1),
(57, '2021-02-21 05:14:05.319455', '2', 'The Pavilion III', 2, '[{\"changed\": {\"fields\": [\"Featured image\", \"Featured image2\", \"Featured image3\", \"Featured image4\", \"Featured image5\", \"Featured image6\", \"Featured image7\", \"Featured image8\", \"Featured image9\", \"Featured image10\"]}}]', 8, 1),
(58, '2021-02-21 05:17:06.727491', '2', 'The Pavilion III', 2, '[{\"changed\": {\"fields\": [\"Featured image4\"]}}]', 8, 1),
(59, '2021-02-21 05:30:00.948624', '2', 'The Pavilion III', 2, '[{\"changed\": {\"fields\": [\"Featured image5\", \"Featured image6\", \"Featured image7\", \"Featured image8\", \"Featured image10\"]}}]', 8, 1),
(60, '2021-02-21 05:30:46.281343', '2', 'The Pavilion III', 2, '[{\"changed\": {\"fields\": [\"Featured image9\"]}}]', 8, 1),
(61, '2021-02-21 08:01:20.663524', '1', 'Document object (1)', 2, '[{\"changed\": {\"fields\": [\"Description\"]}}]', 11, 1),
(62, '2021-02-21 08:01:26.283506', '1', 'Document object (1)', 2, '[]', 11, 1),
(63, '2021-02-21 08:01:34.734833', '2', 'Document object (2)', 2, '[{\"changed\": {\"fields\": [\"Description\"]}}]', 11, 1),
(64, '2021-02-21 08:03:12.532070', '1', 'Sponsor object (1)', 2, '[{\"changed\": {\"fields\": [\"Logo\", \"Description\", \"Experience description\", \"Application overview\", \"Application detail\"]}}]', 12, 1),
(65, '2021-02-22 06:26:22.642095', '10', 'jal2', 3, '', 4, 1),
(66, '2021-02-22 07:19:18.344789', '11', 'jal2', 3, '', 4, 1),
(67, '2021-02-22 07:20:03.026810', '12', 'jal2', 3, '', 4, 1),
(68, '2021-02-22 07:55:02.088004', '13', 'jal2', 3, '', 4, 1),
(69, '2021-02-22 07:55:02.165291', '14', 'Jal3', 3, '', 4, 1),
(70, '2021-02-22 07:55:02.223238', '15', 'jal4', 3, '', 4, 1),
(71, '2021-02-22 14:12:52.821756', '1', 'Document object (1)', 2, '[{\"changed\": {\"fields\": [\"Title\", \"Description\"]}}]', 11, 1),
(72, '2021-02-22 14:13:47.261851', '2', 'Document object (2)', 2, '[{\"changed\": {\"fields\": [\"Title\", \"Description\"]}}]', 11, 1),
(73, '2021-02-22 14:15:12.758850', '1', 'ProspectusDocument object (1)', 2, '[{\"changed\": {\"fields\": [\"Title\"]}}]', 21, 1),
(74, '2021-02-22 14:15:49.284262', '2', 'ProspectusDocument object (2)', 2, '[{\"changed\": {\"fields\": [\"Title\"]}}]', 21, 1),
(75, '2021-02-22 14:17:13.971103', '1', 'Document object (1)', 2, '[{\"changed\": {\"fields\": [\"Title\"]}}]', 11, 1),
(76, '2021-02-22 14:17:25.996457', '2', 'Document object (2)', 2, '[{\"changed\": {\"fields\": [\"Title\"]}}]', 11, 1),
(77, '2021-02-22 14:17:44.778642', '2', 'ProspectusDocument object (2)', 2, '[{\"changed\": {\"fields\": [\"Title\"]}}]', 21, 1),
(78, '2021-02-22 14:17:51.159841', '1', 'ProspectusDocument object (1)', 2, '[{\"changed\": {\"fields\": [\"Title\"]}}]', 21, 1),
(79, '2021-02-22 19:31:02.791499', '2', 'Testimonials object (2)', 2, '[{\"changed\": {\"fields\": [\"Comments\"]}}]', 9, 1),
(80, '2021-02-22 19:31:15.655566', '1', 'Testimonials object (1)', 2, '[{\"changed\": {\"fields\": [\"Comments\"]}}]', 9, 1),
(81, '2021-02-25 18:51:09.477281', '1', 'ProcessFlow object (1)', 1, '[{\"added\": {}}]', 24, 1),
(82, '2021-02-25 18:51:36.707911', '2', 'ProcessFlow object (2)', 1, '[{\"added\": {}}]', 24, 1),
(83, '2021-02-25 19:12:20.141105', '2', 'ProcessFlow object (2)', 2, '[{\"changed\": {\"fields\": [\"Time\"]}}]', 24, 1),
(84, '2021-02-25 19:13:30.416266', '3', 'ProcessFlow object (3)', 1, '[{\"added\": {}}]', 24, 1),
(85, '2021-02-25 19:13:52.502999', '3', 'ProcessFlow object (3)', 3, '', 24, 1),
(86, '2021-02-25 19:25:23.815399', '4', 'ProcessFlow object (4)', 1, '[{\"added\": {}}]', 24, 1),
(87, '2021-02-25 19:40:41.409403', '2', 'ProcessFlow object (2)', 2, '[{\"changed\": {\"fields\": [\"User\"]}}]', 24, 1),
(88, '2021-02-25 19:41:15.487837', '1', 'ProcessFlow object (1)', 2, '[{\"changed\": {\"fields\": [\"User\"]}}]', 24, 1);

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(10, 'home', 'comment'),
(23, 'home', 'companykyc'),
(11, 'home', 'document'),
(7, 'home', 'faq'),
(13, 'home', 'financialmodal'),
(22, 'home', 'individualkyc'),
(24, 'home', 'processflow'),
(19, 'home', 'profile'),
(20, 'home', 'profilefinance'),
(8, 'home', 'property'),
(21, 'home', 'prospectusdocument'),
(12, 'home', 'sponsor'),
(9, 'home', 'testimonials'),
(6, 'sessions', 'session'),
(14, 'social_django', 'association'),
(15, 'social_django', 'code'),
(16, 'social_django', 'nonce'),
(18, 'social_django', 'partial'),
(17, 'social_django', 'usersocialauth');

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-01-28 03:19:40.466955'),
(2, 'auth', '0001_initial', '2021-01-28 03:19:45.629366'),
(3, 'admin', '0001_initial', '2021-01-28 03:20:05.016678'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-01-28 03:20:11.417677'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-01-28 03:20:11.602977'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-01-28 03:20:18.054703'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-01-28 03:20:18.750368'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-01-28 03:20:19.017272'),
(9, 'auth', '0004_alter_user_username_opts', '2021-01-28 03:20:19.209362'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-01-28 03:20:23.456628'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-01-28 03:20:23.662647'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-01-28 03:20:23.772253'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-01-28 03:20:24.196846'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-01-28 03:20:24.316797'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-01-28 03:20:24.608487'),
(16, 'auth', '0011_update_proxy_permissions', '2021-01-28 03:20:24.782473'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-01-28 03:20:25.107838'),
(18, 'home', '0001_initial', '2021-01-28 03:20:29.235572'),
(19, 'sessions', '0001_initial', '2021-01-28 03:20:32.177219'),
(20, 'home', '0002_auto_20210128_0854', '2021-01-28 03:24:38.856165'),
(21, 'home', '0003_auto_20210128_0935', '2021-01-28 04:05:26.452955'),
(22, 'home', '0004_auto_20210128_1913', '2021-01-28 13:44:36.120574'),
(23, 'home', '0005_auto_20210128_2212', '2021-01-28 16:42:45.368792'),
(24, 'home', '0006_auto_20210128_2228', '2021-01-28 16:58:21.132675'),
(25, 'home', '0007_auto_20210128_2319', '2021-01-28 17:49:45.807568'),
(26, 'home', '0008_auto_20210128_2359', '2021-01-28 18:30:02.602583'),
(27, 'home', '0009_property_financial_desclaimer', '2021-01-28 18:49:12.891820'),
(28, 'home', '0010_auto_20210130_1022', '2021-01-30 04:52:24.564961'),
(29, 'home', '0011_auto_20210130_1029', '2021-01-30 04:59:31.727857'),
(30, 'home', '0012_financialmodal', '2021-01-30 05:30:12.605500'),
(31, 'home', '0013_auto_20210130_1103', '2021-01-30 05:33:56.826080'),
(32, 'home', '0014_auto_20210130_1527', '2021-01-30 09:57:36.016123'),
(33, 'home', '0015_auto_20210131_0844', '2021-01-31 03:14:11.471743'),
(34, 'home', '0016_auto_20210131_0846', '2021-01-31 03:17:06.068212'),
(35, 'home', '0017_auto_20210131_0955', '2021-01-31 04:25:38.714235'),
(36, 'default', '0001_initial', '2021-02-03 02:47:09.127176'),
(37, 'social_auth', '0001_initial', '2021-02-03 02:47:09.218698'),
(38, 'default', '0002_add_related_name', '2021-02-03 02:47:14.094604'),
(39, 'social_auth', '0002_add_related_name', '2021-02-03 02:47:14.173331'),
(40, 'default', '0003_alter_email_max_length', '2021-02-03 02:47:14.374896'),
(41, 'social_auth', '0003_alter_email_max_length', '2021-02-03 02:47:14.517254'),
(42, 'default', '0004_auto_20160423_0400', '2021-02-03 02:47:14.589358'),
(43, 'social_auth', '0004_auto_20160423_0400', '2021-02-03 02:47:14.662246'),
(44, 'social_auth', '0005_auto_20160727_2333', '2021-02-03 02:47:14.885237'),
(45, 'social_django', '0006_partial', '2021-02-03 02:47:15.410272'),
(46, 'social_django', '0007_code_timestamp', '2021-02-03 02:47:16.374965'),
(47, 'social_django', '0008_partial_timestamp', '2021-02-03 02:47:17.534986'),
(48, 'social_django', '0009_auto_20191118_0520', '2021-02-03 02:47:18.679872'),
(49, 'social_django', '0010_uid_db_index', '2021-02-03 02:47:19.141266'),
(50, 'social_django', '0005_auto_20160727_2333', '2021-02-03 02:47:19.225488'),
(51, 'social_django', '0004_auto_20160423_0400', '2021-02-03 02:47:19.295021'),
(52, 'social_django', '0002_add_related_name', '2021-02-03 02:47:19.329159'),
(53, 'social_django', '0001_initial', '2021-02-03 02:47:19.361462'),
(54, 'social_django', '0003_alter_email_max_length', '2021-02-03 02:47:19.406912'),
(55, 'home', '0018_profile', '2021-02-07 13:05:26.033206'),
(56, 'home', '0019_auto_20210207_2238', '2021-02-07 17:08:36.627088'),
(57, 'home', '0020_profile_finance', '2021-02-07 17:55:49.631487'),
(58, 'home', '0021_auto_20210207_2337', '2021-02-07 18:07:14.509693'),
(59, 'home', '0022_auto_20210209_1453', '2021-02-09 09:24:06.019620'),
(60, 'home', '0020_remove_profile_us_resident', '2021-02-09 11:34:18.179596'),
(61, 'home', '0021_auto_20210209_1710', '2021-02-09 11:41:01.110423'),
(62, 'home', '0022_auto_20210209_1714', '2021-02-09 11:44:12.334861'),
(63, 'home', '0023_profile_us_citizen', '2021-02-09 12:05:51.536194'),
(64, 'home', '0024_auto_20210209_1800', '2021-02-09 12:30:10.007887'),
(65, 'home', '0025_auto_20210209_1812', '2021-02-09 12:42:55.026637'),
(66, 'home', '0026_auto_20210211_0938', '2021-02-11 04:09:00.011121'),
(67, 'home', '0027_individualkyc', '2021-02-12 06:36:14.488079'),
(68, 'home', '0028_auto_20210212_1303', '2021-02-12 07:33:30.263548'),
(69, 'home', '0029_auto_20210212_1307', '2021-02-12 07:37:53.216026'),
(70, 'home', '0030_companykyc', '2021-02-12 08:11:00.491677'),
(73, 'home', '0031_processflow', '2021-02-25 18:49:55.248931');

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('3e51q7h7qryqp99w31zjke0zr48nnvbf', 'eyJmYWNlYm9va19zdGF0ZSI6InVtWmNCMENWVkpzYW1tRlNSZkFSWVdsclR0VXRSU2JqIn0:1lAljn:OwKH_X-Igqu5dpl_zcmaZmfO1L-la1j8ZC8bvFnDLBQ', '2021-02-27 03:36:51.863385'),
('3l5tczp8ur2ap1u04ny2ly8rr90bgioy', '.eJxVjMsKwjAQRf8laylNGxPjThFBRFRcaFdlZjKxtdJoHwiK_65CN27vOee-hAdiDKHK2w46FlOxr2mcrk7X2fph7rJ4Zje3W-hmuzziITvKkxiJHPquyPuWm7x030T-bwhUcf0D7gL1OUQU6q4pMfop0UDbaBMcX-eD-3dQQFt8a_ZGAyVWuQmQktKSQYuWCG0ykYZdEmtvbcpeJRA7BRhbgyr1wFrqGMX7A2aJSac:1lAn6I:HwVk154xNUR4tV9AOCCKksHAEPodn4pDGMaYcnP8hn4', '2021-02-27 05:04:10.487447'),
('4w0fxm7v46msjwj04ra2z6ai18zuyuw5', '.eJxVjEEOwiAQRe_C2hAYaAGX7j0DmRlAqqYkpV0Z765NutDtf-_9l4i4rTVuPS9xSuIstDj9boT8yPMO0h3nW5Pc5nWZSO6KPGiX15by83K4fwcVe_3WHsYUrGZjFRmjiU0BF4BGcEhc2HkHBQFDMioM5AcsalSQiXNhG1i8P9ViOCo:1lFMUH:-crnZRmm0FJ4XfXiG6B_MDhou-tAwjG5qkD8yjfkAmw', '2021-03-11 19:39:49.764561'),
('4wnwm38pj3lylcdzjgtiavv13ccmoeyl', '.eJxVjEEOwiAQRe_C2hAYaAGX7j0DmRlAqqYkpV0Z765NutDtf-_9l4i4rTVuPS9xSuIstDj9boT8yPMO0h3nW5Pc5nWZSO6KPGiX15by83K4fwcVe_3WHsYUrGZjFRmjiU0BF4BGcEhc2HkHBQFDMioM5AcsalSQiXNhG1i8P9ViOCo:1lFAQs:RwFrJL2Hi7PeC_fD-grCaKFDQi-Ta7cAIkMMYDiapNE', '2021-03-11 06:47:30.915282'),
('4wopptp37e36iz4z8cdcnzz99kqd528j', 'eyJnb29nbGUtb2F1dGgyX3N0YXRlIjoiclIxQjdocVdWdTJJMFdHeDhlMWZ1anYxWko4N0dwU1QifQ:1lCDoc:TLzBvac0c_26mfG94tdiJ_bdKIInc5_QL92pkKFAmvs', '2021-03-03 03:47:50.400199'),
('8gvzvxqvwjkknykg6dtlommh6p68tt93', '.eJxVjEEOwiAQRe_C2hCgBDou3XsGMjMMUjU0Ke3KeHdt0oVu_3vvv1TCba1p67KkKauzsur0uxHyQ9oO8h3bbdY8t3WZSO-KPmjX1znL83K4fwcVe_3WUmJAduDziOytBY4EBMwEbrRRsjOhAAxSvEOTPZKBSH4oKMEGQ-r9AfxJOGc:1l5llh:Hfz6jCO5uPp0wps8DO75xoe1VBKWmsLApQb_fxSMhKQ', '2021-02-13 08:38:09.217907'),
('anc62ofj5gpd6w7jk5hf4iljrr5jzb38', '.eJxVjEEOwiAQRe_C2hAYaAGX7j0DmRlAqqYkpV0Z765NutDtf-_9l4i4rTVuPS9xSuIstDj9boT8yPMO0h3nW5Pc5nWZSO6KPGiX15by83K4fwcVe_3WHsYUrGZjFRmjiU0BF4BGcEhc2HkHBQFDMioM5AcsalSQiXNhG1i8P9ViOCo:1lES0a:ySCwaGj8A_kb3Cr9c7s76nFRypadytfpLzPndCiAQQY', '2021-03-09 07:21:24.160085'),
('c13mrf7nwuqy9xx1vls46qxwfliwe22s', '.eJxVjFtLwzAYhv9LrqUkaWgW76agjFFPVTzclO_LYaktDbbJVif77-tgiN6-z_s8P6SGFH2dRjvUjSGXhJGLvxuCbm1_AuYT-k3IdOjj0GB2umRnOmZlMLa7On__BTyMfratkwVoroRZgBaMKS1RodIaFV8waQ2nhVMqt05woEYAUiVR5A5swQqKc9SBthhCW48Rop2bL69r_oZMbJMUU8lKw3S121fLocrbtXrfzc6miT7hr9Hc8_2I8mn1_N3dPvg7vnr8SNvOFcsvOk3XN-RwBD5VWm0:1lA5QM:o-lsAag-LUr2-drN4M4bZXKsuAZL78QhHxTGKuRtRl8', '2021-02-25 06:25:58.691734'),
('c40w7jq71dz1yyk8midsnlf3uf7a0en1', '.eJxVjF0LgjAYRv_LrmO4uabrMvImiyAy6Ered5sfZRpuEhT99xS88fY55zxfUta-GjB3HrwlG5Kx0_WlYX9utlmSfGQ3pLv6LdaXhB_SG3uSFclh8FU-ONvntRkTttwQ9MO2EzB3aMuO6q71fY10UuhMHT12xjbb2V0cVOCqsbZFJEFzJUwMWjCmdIQKldaoeMwia3ggC6VCWwgOgRGAgYpQhAVYyWSA5PcHk11IpQ:1lAPzx:CWxu_BUG5sMot_hnGKeKOTf7fpaWev1tuh28UYR9hHs', '2021-02-26 04:24:05.296980'),
('c61yld3yggpt1riirxy0fit5ws2r56s9', '.eJxVjEEOwiAQRe_C2hCgBDou3XsGMjMMUjU0Ke3KeHdt0oVu_3vvv1TCba1p67KkKauzsur0uxHyQ9oO8h3bbdY8t3WZSO-KPmjX1znL83K4fwcVe_3WUmJAduDziOytBY4EBMwEbrRRsjOhAAxSvEOTPZKBSH4oKMEGQ-r9AfxJOGc:1l9Kqb:A6lWBfvALtS2Fl2v2HAYO9YgOMvStwtI9GGxKhKX0RI', '2021-02-23 04:41:57.898611'),
('eabkna31gi0ousdkicr2cylg6jutdccq', '.eJxVjEEOwiAQRe_C2hAYaAGX7j0DmRlAqqYkpV0Z765NutDtf-_9l4i4rTVuPS9xSuIstDj9boT8yPMO0h3nW5Pc5nWZSO6KPGiX15by83K4fwcVe_3WHsYUrGZjFRmjiU0BF4BGcEhc2HkHBQFDMioM5AcsalSQiXNhG1i8P9ViOCo:1lE6f7:LFFwXYeR2uWlojtgkvUQ6M1mZEE_Hxh1oeNzIxj2r8E', '2021-03-08 08:33:49.079082'),
('jbiu2yoh2s2jco3enz0n01lewdg8mqjg', '.eJxVjMsOgjAQRf-layUw5VWXyIKYaGL4ADIzbQEhNPLYYPx3IXGh23vOPS9R4TI31TKZsWq1OIlAHH43Qu7MsAP9wKF2HrthHlvydsX70sm7Om367Ov-BRqcmu2dQqxVGLAMfZIyIJYWEgUUQ4LElpM0AYuASktfRZRGaP3YB0NsLIeKt2jtXN2bo9vbUE0zzmYL3-p7y2saXdZzkzubdVavQ5m3z5IKQCjE-wOQSkuw:1lEEpP:1F2S0QruO43xhXD_RBqGBAkIA4yuGQoJi97INvReLTQ', '2021-03-08 17:16:59.642374'),
('klrtcydfc6t7tiw8kcmn14g3hno8neol', '.eJxVjL0OgjAURt-lsxLKhQKOLIZBEwk7ue1tAflphDIQ47sLCYOu3znfebMKF9dUy6ynqiV2YZydfjeJqtPjDuiJY209ZUc3tdLbFe-gs3ezpPvscP8CDc7N9o5AxuQbkIZ4AAIwiDlXKEMDaaKSmAQCCQiVSIkT-lEsIdUygkgYzhOzRWtr616f7d4Oqtmh01vYdQMERZ7cxdry8jGsWExpjur6KmWblQP7fAF_SEsj:1lBWlf:7JtX_0eKvsytFZv-HAJP8EqPQnss6RhZkgvHtmEVkJI', '2021-03-01 05:49:55.408878'),
('l43lhcetjmtw7k2aioy4t2y5ftx3rj92', '.eJxVjDGPgkAQRv_L1ieBWWRZO7VQk7vEwsuVZGZ2FlRkDSzVxf8uJBR37ffe935VhWNsqnGQvro6tVGZ-vi7EfJduhm4G3Z1SDh0sb9SMivJQofkKzhpd4v7L9Dg0EzvEgpn84x1npLWGbH2YCxQAQaJPZvSgEdA63Rq11Su0adFCkIsnnPLU7QOoW5lFeY2VEPEKFM4xjg-_JNO37S17flT9j8GxO2Px0s8lOjU6w2Vr0ud:1lEPfv:yYobyQyup1O-Mq_aMJcHOFaPHlAI5dOD3EkE-qy-A_w', '2021-03-09 04:51:55.986707'),
('lpjtl5ui34d60x1u5o0y4884869qcw4e', '.eJxVjEEOwiAQRe_C2hCgBDou3XsGMjMMUjU0Ke3KeHdt0oVu_3vvv1TCba1p67KkKauzsur0uxHyQ9oO8h3bbdY8t3WZSO-KPmjX1znL83K4fwcVe_3WUmJAduDziOytBY4EBMwEbrRRsjOhAAxSvEOTPZKBSH4oKMEGQ-r9AfxJOGc:1l4xvm:H0TYHxvZUb__lj1XjzioL_Q0dhKOv74JhLoVN9Um-Nw', '2021-02-11 03:25:14.993367'),
('lr0rlrilvx5nh5l0y0gro2o0j014nkme', 'e30:1l96gl:vwdJulzWrmx0l9FMofj0dKF9PXoLYMnf0FaGCIV7XtM', '2021-02-22 13:34:51.000049'),
('nigneskali63wz0im2q7vqnf2clnrzaj', 'e30:1l96g4:pz2pKgxu_rOjvy-84xqWAoepLadrxPqJuM6jqVVGbks', '2021-02-22 13:34:08.301980'),
('pe8m7xikalkrixtfysz63sujbnbzpux1', '.eJxVjEEOwiAQRe_C2hAYaAGX7j0DmRlAqqYkpV0Z765NutDtf-_9l4i4rTVuPS9xSuIstDj9boT8yPMO0h3nW5Pc5nWZSO6KPGiX15by83K4fwcVe_3WHsYUrGZjFRmjiU0BF4BGcEhc2HkHBQFDMioM5AcsalSQiXNhG1i8P9ViOCo:1lDgkj:npM9nkKliYsgDt1SKnd47IEMVlTgOnPN6F9WQSNHI38', '2021-03-07 04:53:53.845702'),
('qzixp2al74spm7v2z5fmmqz6lmh8s7va', '.eJxVjEEOwiAQRe_C2hCgBDou3XsGMjMMUjU0Ke3KeHdt0oVu_3vvv1TCba1p67KkKauzsur0uxHyQ9oO8h3bbdY8t3WZSO-KPmjX1znL83K4fwcVe_3WUmJAduDziOytBY4EBMwEbrRRsjOhAAxSvEOTPZKBSH4oKMEGQ-r9AfxJOGc:1l576X:rDxGA-n4AfeH1reKwNHP_1WEEaa0jqlqQpOrrYrSD94', '2021-02-11 13:12:57.140080'),
('rmie72hfajonqb89i53lvmoz0yv9xwp2', '.eJxVjEEOwiAQRe_C2hCgBDou3XsGMjMMUjU0Ke3KeHdt0oVu_3vvv1TCba1p67KkKauzsur0uxHyQ9oO8h3bbdY8t3WZSO-KPmjX1znL83K4fwcVe_3WUmJAduDziOytBY4EBMwEbrRRsjOhAAxSvEOTPZKBSH4oKMEGQ-r9AfxJOGc:1l7b9A:Hi2MU-ra9EMRnLrmz-R-Hr-I5hoq3oRvxWnNxaggPVs', '2021-02-18 09:41:56.518468'),
('s98ftexvcczvd0hogf4tbk5yuby8j473', 'e30:1l96dq:1_Vkg-X39dmQ-eNetsqyf8ROrr_jA-4W1los3c7Sr-I', '2021-02-22 13:31:50.170090'),
('vqqkl9w5zoa8jcrluyrksq1yh8om743w', '.eJxVjEEOwiAQRe_C2pCCHWBcuu8ZyMCMUjU0Ke3KeHfbpAvdvvf-f6tI61Li2mSOI6uLMur0yxLlp9Rd8IPqfdJ5qss8Jr0n-rBNDxPL63q0fweFWtnWBA64oyCZMHlrOYgT4IweN2SMRQM3352DT8x9ZuMS9s6JEQteENTnC_fEOBk:1lCb3p:xS5NOzJAgwCbB2tlnrSZ-9HxlVZokzySl_kN0PQpw5s', '2021-03-04 04:37:05.677630'),
('w6ky8rwhlxe3xnyepwaonglehzanmrzd', '.eJxVjEEOwiAQRe_C2hCgBDou3XsGMjMMUjU0Ke3KeHdt0oVu_3vvv1TCba1p67KkKauzsur0uxHyQ9oO8h3bbdY8t3WZSO-KPmjX1znL83K4fwcVe_3WUmJAduDziOytBY4EBMwEbrRRsjOhAAxSvEOTPZKBSH4oKMEGQ-r9AfxJOGc:1lAPzx:4IX6m-k54RYmcEOE12uz6gSz4_nRgpWgnxYpQz1BLkQ', '2021-02-26 04:24:05.306807'),
('yi7xv0zzix6izku8k9jfx1v5zhaq5ysk', '.eJxVkMkKwjAURf8lay1JTDO4E8QBQbtQdBcydcDaSJMKIv67Vl3Y1YP7OPc83gMU3he1G3vVxRLLEFV0YAoO12Y_5_DU3fO4KRfFAW5veAVXmV9fjhkSYARkT8guuFZW9o3wYaaVObumXwRvKlVL41uX_NKQfLXJ8jN2s14-5EsVyjesqcihtUQLRzljkxQzSgxP7cRYbBkilDAOMWJCE2sIoTYnECmc8lQhofvSn_9TXasQZe2Lqvk7cPAC8HwBO-5bkw:1lCDpC:0-QdcKPBZk-gr44Fl9M-DfLkdIl_ACA-9gRWQwkE1Mc', '2021-03-03 03:48:26.840363'),
('yppybc3nm7e1bf91x71peks0rm8a041g', '.eJxVjL0OwiAURt-F2TTQEihudjI29SeNM7kXLlZtStKCi_Hd1cTF9TvnfE8WwBHGeLdLgkRszeZ2yNv-1Gx6fmhVA-KWd7Eb9b7O1fFxvrAVs5DTYPNCs736TyL-NwR3p-kL_A2mSyxcnNJ8xeKrFD-6FF30NDY_9-9ggGX41BS0Alca6WtwUgjjNBo0zqEpa6HJl1wFYyoKsgTuJSA3GmUVgJRQHNnrDUGwSXc:1lAmub:19Lw51X-xy85zh_zbj-QXNYqs3yJsyLmJ0PlCljj77A', '2021-02-27 04:52:05.619232'),
('zo0jh5c1p83jmgv3o8l100nbxbcdex77', '.eJxVjMsKwjAQRf8laylNG5uOSxURxJ2L7spMMjG22oCJDxD_3RZc6Paec89LtHhLvr1FvrYnKxZCitnvRmh6HiZgOxyOITNhSNcTZZOSfWnM9sHyefl1_wIeox_f7HSFpgBlazRKSjCagMAYgqKWmm2RVw6gZKcKzK1CykGTKh1yJaucxqhDwxRC38aEicdmA9gNz6Z-zku_vnu9SrDc2eNhtXmct5cQxfsDQjFKIQ:1l8kDz:4qDiDsWJvwI1MRnzDeFekbKwJOyf3k4sWSeJY0tCBv0', '2021-02-21 13:35:39.666575'),
('zsrqsmug0d6irnyac2l3rr6yp7aai6mh', '.eJxVjEEOwiAQRe_C2pCCHWBcuu8ZyMCMUjU0Ke3KeHfbpAvdvvf-f6tI61Li2mSOI6uLMur0yxLlp9Rd8IPqfdJ5qss8Jr0n-rBNDxPL63q0fweFWtnWBA64oyCZMHlrOYgT4IweN2SMRQM3352DT8x9ZuMS9s6JEQteENTnC_fEOBk:1lCMN4:i9RBY0uSchcYaSpAWSaxGCGoaf_rg1_OrdGtXcUmMNI', '2021-03-03 12:55:58.176533');

--
-- Dumping data for table `home_document`
--

INSERT INTO `home_document` (`id`, `title`, `description`, `document`, `property_id`) VALUES
(1, 'Sample 1', 'Association with Tier 1 law firms to mitigate legal risk and thorough evaluation of properties with IPC Property Listing Less than 2% of the properties analyzed are listed', 'document/file-sample_100kB.doc', 1),
(2, 'Sample 2', 'Detailed analysis of micro market, rentals, tenant credit worthiness, asset quality and lease agreement robustness', 'document/file-sample_100kB_kPVOVgC.doc', 1);

--
-- Dumping data for table `home_faq`
--

INSERT INTO `home_faq` (`id`, `question`, `answer`) VALUES
(1, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis nisi magna. Proin eget elit lectus', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis nisi magna. Proin eget elit lectus. Sed mi metus, vehicula ac tortor vitae, tempus molestie ex.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis nisi magna. Proin eget elit lectus. Sed mi metus, vehicula ac tortor vitae, tempus molestie ex.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis nisi magna. Proin eget elit lectus. Sed mi metus, vehicula ac tortor vitae, tempus molestie ex.'),
(2, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis nisi magna. Proin eget elit lectus', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis nisi magna. Proin eget elit lectus. Sed mi metus, vehicula ac tortor vitae, tempus molestie ex.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis nisi magna. Proin eget elit lectus. Sed mi metus, vehicula ac tortor vitae, tempus molestie ex.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis nisi magna. Proin eget elit lectus. Sed mi metus, vehicula ac tortor vitae, tempus molestie ex.'),
(3, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis nisi magna. Proin eget elit lectus', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis nisi magna. Proin eget elit lectus. Sed mi metus, vehicula ac tortor vitae, tempus molestie ex.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis nisi magna. Proin eget elit lectus. Sed mi metus, vehicula ac tortor vitae, tempus molestie ex.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed quis nisi magna. Proin eget elit lectus. Sed mi metus, vehicula ac tortor vitae, tempus molestie ex.Lorem ipsum dolor sit amet, c');

--
-- Dumping data for table `home_financialmodal`
--

INSERT INTO `home_financialmodal` (`id`, `title`, `day0`, `year1`, `year2`, `year3`, `year4`, `year5`, `property_id`) VALUES
(1, 'INVESTMENT', '20000', '', '', '', '', '', 1),
(2, 'Rents', '20000', '20000', '20000', '20000', '', '20000', 1),
(3, 'Sale Value', '20000', '', '', '20000', '20000', '', 1);

--
-- Dumping data for table `home_processflow`
--

INSERT INTO `home_processflow` (`id`, `name`, `date`, `time`, `user_id`) VALUES
(1, 'Process Flowchart', '2021-02-25', '18:51:05.000000', 1),
(2, 'Prospectus', '2021-02-25', '19:12:17.000000', 1),
(4, 'jal singh', '2021-02-25', '19:25:20.000000', 16);

--
-- Dumping data for table `home_profile`
--

INSERT INTO `home_profile` (`id`, `residence_country`, `ssn`, `phone`, `doc_proof`, `user_id`, `us_resident`, `ownership_type`, `us_citizen`, `accreditation`, `custodial_account`, `ssn_taxid`, `investment_experience`, `previously_invested`) VALUES
(1, 'India', '12312', '123456789012', 'UserProfile/image034.jpg', 1, 1, 'individual', '1', '3', '1', '1', '4', '4'),
(7, '', '', '', '', 9, 0, 'individual', '', '1', '', '', '1', '1'),
(14, '', '', '', '', 16, 0, 'individual', '', '1', '', '', '1', '1'),
(15, '', '', '', '', 17, 0, 'individual', '', '1', '', '', '1', '1'),
(16, '', '', '', '', 18, 0, 'individual', '', '1', '', '', '1', '1'),
(17, '', '', '', '', 19, 0, 'individual', '', '1', '', '', '1', '1');

--
-- Dumping data for table `home_property`
--

INSERT INTO `home_property` (`id`, `name`, `description`, `address`, `price`, `tags`, `property_type`, `email`, `bedrooms`, `bathrooms`, `halls`, `kitchens`, `area`, `property_id`, `year_built`, `contact`, `lot_dimensions`, `deposit_amount`, `is_fav`, `featured_image`, `images`, `about_builder`, `financial`, `due_diligence`, `property_details`, `updates`, `doc_reports`, `location`, `map_location`, `location_detail`, `localty`, `storeys`, `parking`, `floor_for_sale`, `parking_ratio`, `floor_efficiency`, `fit_outs`, `total_area`, `power_area`, `power_backup`, `area_of_sale`, `air_conditioning`, `purchase_price`, `stamp_duty`, `brokerage`, `legal_fees`, `reserves`, `highlights`, `featured_image10`, `featured_image2`, `featured_image3`, `featured_image4`, `featured_image5`, `featured_image6`, `featured_image7`, `featured_image8`, `featured_image9`, `financial_desclaimer`, `acquisition`, `acquisition_frequency`, `asset_management`, `asset_management_frequency`, `asset_risk`, `asset_type`, `expected_holding_period`, `expected_irr`, `funded_member`, `minimum_investment`, `total_deal_size`, `total_sft`) VALUES
(1, 'Property one', 'Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero\'s De Finibus Bonorum et Malorum for use in a type specimen book.', 'Cecilia Chapman 711-2880 Nulla St. Mankato Mississippi 96522 (257) 563-7401', '250000', 'For Sale', 'For sale', 'test38@mailinator.com', '4', '5', '2', '1', '3500', '2544', '2014', 'Contact', '152', '20000', 0, 'featured_image/199c514e38ce3993a549e353d96cc724.jpg', 'False', 'What is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make a type specimen book it has?', 'FalWhat is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make a type specimen book it has?What is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to se', 'What is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make a type specimen book it has?What is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make', 'What is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make What is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make a type specimen book it has?', 'What is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make a type specimen book it has?What is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make', 'False', 'Hydrabad', '12.253.55', 'What is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make a type specimen book it has?', 'Karmandan', '2', 'Yes', '2', '1:25', '25%', '63', '15200', '1500', '100%', '12000', 'Yes', '1500000', '2500', '3000', '1000', '1520', 'What is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make a type specimen book it has?What is Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and typesetting industry Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s when an unknown printer took a galley of type and scrambled it to make a type specimen book it has?', 'featured_image/a348af673e463b482529099fd4524a93_jKE5lnj.jpg', 'featured_image/a348af673e463b482529099fd4524a93.jpg', 'featured_image/banner-2.jpg', 'featured_image/c5c068f92057a049dcd12e598a589718.jpg', 'featured_image/a348af673e463b482529099fd4524a93_ufnUxXA.jpg', 'featured_image/banner-2_Bwk3PNV.jpg', 'featured_image/199c514e38ce3993a549e353d96cc724_2PleueL.jpg', 'featured_image/banner-2_G2cp9RB.jpg', 'featured_image/a348af673e463b482529099fd4524a93_RhS4uxR.jpg', 'Generate Lorem Ipsum placeholder text for use in your graphic, print and web layouts, and discover plugins for your favorite writing, design and blogging tools.', '2% of Property Acquisition Price', 'One Time', '0.5% of Property Acquisition Price (charged monthly)', 'Annual', 'Low Risk', 'Commercial', '5 Years', '19%', '700', '100$', '6,50,000', '6,50,000'),
(2, 'The Pavilion III', 'There is an opportunity to purchase 52,277 sf in The Pavilion on Outer Ring Road, Bangalore tenanted to Singapore-based Aurbis Business Parks for an all-in cost of Rs. 69,90,00,000 (Rs. 12,338 per sf) implying a 9.14% yield and 18% IRR for Pre-book investors.  The Pavilion is a newly-built 210,000 sf Grade A office asset on Outer Ring Road, Bangalore fully leased to Aurbis Business Parks with a 5-year lock-in. Aurbis has in-turn leased to blue-chip tenants including Tata Technologies, eBay, Livspace,', 'Outer Ring Road, Bangalore', '500000', 'For Sale', 'For Sale', 'Pavailion@gmail.com', '5', '4', '2', '1', '2000', '1245', '2015', 'Contact', '152', '100000', 0, 'featured_image/199c514e38ce3993a549e353d96cc724_l38Teha.jpg', 'False', 'With a firm existence for more than three decades in the real estate sector of Rajasthan, Mahima Group has successfully established 30 years of presence across the various verticals of infrastructural development. Having completed and delivered 8 Million Sq. Ft of area, currently, the firm has 3.16 Million Sq. ft. under construction. We have delivered timeless quality in the commercial developments with the four most popular Commercial Complexes that have now turned into the landmarks of the city. Not only', 'Economic discrimination is discrimination based on economic factors. These factors can include job availability, wages, the prices and/or availability of goods and services, and the amount of capital investment funding available to minorities for business.', 'Economic discrimination is discrimination based on economic factors. These factors can include job availability, wages, the prices and/or availability of goods and services, and the amount of capital investment funding available to minorities for business.', 'The Pavilion is a newly-built 210,000 sf Grade A office asset on Outer Ring Road, Bangalore fully leased to Aurbis Business Parks with a 5-year lock-in. Aurbis has in-turn leased to blue-chip tenants including Tata Technologies, eBay, Livspace,', 'False', 'The Pavilion is a newly-built 210,000 sf Grade A office asset on Outer Ring Road, Bangalore fully leased to Aurbis Business Parks with a 5-year lock-in. Aurbis has in-turn leased to blue-chip tenants including Tata Technologies, eBay, Livspace,', 'Outer Ring Road, Bangalore', '12.9716,77.5946', 'Outer Ring Road is the largest office market in Bangalore with headquarters of tenants like Microsoft, Goldman Sachs, JP Morgan, Northern Trust, Cisco, Oracle, Wells Fargo and LinkedIn among others.', 'Banglore', '3', 'Yes', '2', '1:1', '25%', '63', '2200', '100', 'Yes', '2200', 'Available', '490000', '2500', '3000', '1000', '1520', 'The Pavilion is a newly-built 210,000 sf Grade A office asset on Outer Ring Road, Bangalore fully leased to Aurbis Business Parks with a 5-year lock-in. Aurbis has in-turn leased to blue-chip tenants including Tata Technologies, eBay, Livspace,', 'featured_image/a348af673e463b482529099fd4524a93_piAqExH.jpg', 'featured_image/a348af673e463b482529099fd4524a93_bBmRcsd.jpg', 'featured_image/banner-2_71zBdMY.jpg', 'featured_image/banner-2_G2cp9RB_r50JDmM.jpg', 'featured_image/banner-2_71zBdMY_zMQ8RC0.jpg', 'featured_image/a348af673e463b482529099fd4524a93_0sbQhBN.jpg', 'featured_image/banner-2_jdgytvd.jpg', 'featured_image/Nayara_Slider_hR5CoLB.gif', 'featured_image/banner-2_bIVM5YK.jpg', 'Economic discrimination is discrimination based on economic factors. These factors can include job availability, wages, the prices and/or availability of goods and services, and the amount of capital investment funding available to minorities for business.', '2% of Property Acquisition Price', 'One Time', '0.5% of Property Acquisition Price (charged monthly)', 'Annual', 'Low Risk', 'Domestic', '5 Years', '19%', '2', '100$', '2200', '2200');

--
-- Dumping data for table `home_prospectusdocument`
--

INSERT INTO `home_prospectusdocument` (`id`, `title`, `document`, `property_id`) VALUES
(1, 'Sample 2', 'prospectus/document/file-sample_100kB.doc', 1),
(2, 'Sample 1', 'prospectus/document/file-sample_100kB_w8Fq0zh.doc', 1);

--
-- Dumping data for table `home_sponsor`
--

INSERT INTO `home_sponsor` (`id`, `title`, `description`, `property_id`, `application_detail`, `application_name`, `application_overview`, `document`, `experience_description`, `experience_tag`, `experience_title`, `logo`, `location`) VALUES
(1, 'sohini tesh Park', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed a varius leo. Nunc eget vehicula velit. Pellentesque sodales enim in erat consectetur ultricies.Lorem ipsum dolor sit amet, consectetur', 1, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed a varius leo. Nunc eget vehicula velit. Pellentesque sodales enim in erat consectetur ultricies.Lorem ipsum dolor sit amet, consectetur a', 'Thomus routers clear', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed a varius leo. Nunc eget vehicula velit. Pellentesque sodales enim in erat consectetur ultricies.Lorem ipsum dolor sit amet, consectetur a', 'sponsor_document/New_Text_Document_10.txt', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed a varius leo. Nunc eget vehicula velit. Pellentesque sodales enim in erat consectetur ultricies.Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed a varius leo. Nunc eget vehicula velit. Pellentesque sodales enim in erat consectetur', '30 Years Combined', 'Over ten year principal experience', 'sponsers/demoLogo.png', 'Hydrabaad');

--
-- Dumping data for table `home_testimonials`
--

INSERT INTO `home_testimonials` (`id`, `name`, `designation`, `image`, `comments`) VALUES
(1, 'Akhilesh Bodhi', 'CEO', 'testimonials/WhatsApp_Image_2020-07-14_at_12.21.27_PM.jpeg', 'Would this be ok with you? If this makes you even a little bit uncomfortable, no worries at all. But if you are ok with it, I can send you a very short blurb for you to review, or you can write a sentence or two and send it over. Whatever is easiest for you.'),
(2, 'Jal singh', 'CEO at TestCompany', 'testimonials/rsz_whatsapp_image_2020-07-14_at_122127_pm.jpg', 'I’m writing to ask if you wouldn’t mind giving us a short testimonial for our website. We’re updating a few pages, and I’m hoping to add something from you. It would link back to your site, so it’s actually a good thing for your SEO.');

--
-- Dumping data for table `social_auth_usersocialauth`
--

INSERT INTO `social_auth_usersocialauth` (`id`, `provider`, `uid`, `extra_data`, `user_id`, `created`, `modified`) VALUES
(8, 'google-oauth2', 'jlsingh38@gmail.com', '{\"auth_time\": 1613809709, \"expires\": 3598, \"token_type\": \"Bearer\", \"access_token\": \"ya29.A0AfH6SMALCrGz_C1HkeeiiYdtxDnmeSSK15D2YQ3yJKHpC6ugxJPPDp9RIKm2FpcZg4VSLbmtxt4YPJh_FAeGG9XQci8sG-EgAmQ4c3Un2Jxtl_ns6_I-AkZuT35l9aeN3oebkC9F-N9OJQaWDjLO0j2IkglcnQ\"}', 9, '2021-02-17 13:05:25.051348', '2021-02-20 08:28:29.434378'),
(9, 'facebook', '3679796522108857', '{\"auth_time\": 1613741908, \"id\": \"3679796522108857\", \"expires\": 5183998, \"granted_scopes\": [\"public_profile\"], \"denied_scopes\": null, \"access_token\": \"EAAHjMiJdKSgBABMdgcTHuzd8OCO0i4klsGATydzXsccyE8oIHJYCNyi418y7xhfr9FlaJmZBkRGNkkYVIot3yt3u4A2yUbCAy7YMN9izDcwlLeCgaTt8IQYUctM9V5TvYGVXzHAYsRnC2qlFZClcNts8ndYHzZCblIi3eE8uQZDZD\", \"token_type\": null}', 9, '2021-02-17 13:06:06.738714', '2021-02-19 13:38:28.798119');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
