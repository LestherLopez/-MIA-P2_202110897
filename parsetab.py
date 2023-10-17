
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD BESTFIT BYTES CADENA CONT DELETE ENTERO EXECUTE EXTENDED FDISK FIRSTFIT FIT FS FULL GUION ID IDDISK IGUAL KILOBYTE LOGIC LOGIN LOGOUT MAYOR_QUE MEGABYTE MKDIR MKDISK MKFILE MKFS MKGRP MOUNT NAME PASS PATH PAUSE PM PRIMARY R REP RMDISK ROUTE RUTA SIZE TYPE UNIT UNMOUNT USER WORSTFITinit : list_commandslist_commands : list_commands commands\n                    | commandscommands : command_mkdisk\n                | command_rmdisk\n                | command_fdisk\n                | command_mount\n                | command_unmount\n                | command_mkfs\n                | command_execute\n                | command_rep\n                | PartitionsMount\n                | command_login \n                | command_logout\n                | command_mkgrp\n                | command_mkfile\n                | command_mkdir\n                | command_pausePartitionsMount : PMcommand_mkdisk : MKDISK parameters_mkdiskparameters_mkdisk : parameter_mkdisk parameters_mkdisk\n                        |parameter_mkdisk : GUION SIZE IGUAL ENTERO\n                        | GUION PATH IGUAL ROUTE\n                        | GUION FIT IGUAL fit_options\n                        | GUION UNIT IGUAL unit_options\n                        command_pause : PAUSEcommand_rmdisk : RMDISK GUION PATH IGUAL ROUTE command_fdisk : FDISK parameters_fdiskparameters_fdisk : parameter_fdisk parameters_fdisk\n                        |parameter_fdisk : GUION SIZE IGUAL ENTERO\n                      | GUION PATH IGUAL ROUTE\n                      | GUION NAME IGUAL ID\n                      | GUION UNIT IGUAL unit_options\n                      | GUION TYPE IGUAL type_options\n                      | GUION FIT IGUAL fit_options\n                      | GUION DELETE IGUAL FULL\n                      | GUION ADD IGUAL ENTEROcommand_mount : MOUNT parameters_mountparameters_mount : parameter_mount parameters_mount\n                        |parameter_mount :  GUION PATH IGUAL ROUTE\n                        | GUION NAME IGUAL ID\n                        command_unmount : UNMOUNT GUION IDDISK IGUAL ENTERO IDcommand_mkfs : MKFS parameters_mkfsparameters_mkfs : parameter_mkfs parameters_mkfs\n                        |parameter_mkfs : GUION IDDISK IGUAL ENTERO ID\n                     | GUION TYPE IGUAL FULL\n                     | GUION FS IGUAL ENTERO FScommand_login : LOGIN parameters_loginparameters_login : parameter_login parameters_login\n                        | parameter_login : GUION IDDISK IGUAL ENTERO ID\n                        | GUION USER IGUAL ID\n                        | GUION PASS IGUAL ENTERO\n                        | GUION PASS IGUAL IDcommand_logout : LOGOUTcommand_mkgrp : MKGRP GUION NAME IGUAL IDcommand_mkfile : MKFILE parameters_mkfileparameters_mkfile : parameter_mkfile parameters_mkfile\n                        |parameter_mkfile : GUION PATH IGUAL ROUTE\n                        | GUION SIZE IGUAL ENTERO\n                        | GUION CONT IGUAL ROUTE\n                        | GUION Rcommand_mkdir : MKDIR parameters_mkdirparameters_mkdir : parameter_mkdir parameters_mkdir\n                        |parameter_mkdir : GUION PATH IGUAL ROUTE\n                        | GUION Rcommand_execute : EXECUTE GUION PATH IGUAL ROUTEcommand_rep : REP parameters_repparameters_rep : parameter_rep parameters_rep\n                       | parameter_rep  :  GUION PATH IGUAL ROUTE\n                        | GUION IDDISK IGUAL ENTERO ID\n                        | GUION NAME IGUAL ID\n                        | GUION RUTA IGUAL ROUTE fit_options : FIRSTFIT\n                    | BESTFIT\n                    | WORSTFITunit_options : KILOBYTE\n                    | MEGABYTE\n                    | BYTEStype_options : PRIMARY \n                    | EXTENDED\n                    | LOGIC'
    
_lr_action_items = {'MKDISK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'RMDISK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'FDISK':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'MOUNT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'UNMOUNT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'MKFS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'EXECUTE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'REP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'PM':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[27,27,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'LOGIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[28,28,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'LOGOUT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[29,29,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'MKGRP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[30,30,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'MKFILE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[31,31,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'MKDIR':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[32,32,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'PAUSE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[33,33,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,24,26,27,28,29,31,32,33,34,35,36,39,40,42,43,46,47,50,51,53,54,57,58,60,61,63,69,78,82,87,92,97,101,102,104,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,163,165,166,168,169,171,172,173,174,175,176,177,178,179,180,181,182,183,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-22,-31,-42,-48,-76,-19,-54,-59,-63,-70,-27,-2,-20,-22,-29,-31,-40,-42,-46,-48,-74,-76,-52,-54,-61,-63,-68,-70,-21,-30,-41,-47,-75,-53,-62,-67,-69,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-28,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-73,-77,-79,-80,-56,-57,-58,-60,-64,-65,-66,-71,-45,-49,-51,-78,-55,]),'GUION':([19,20,21,22,23,24,25,26,28,30,31,32,36,40,43,47,51,54,58,61,101,104,137,138,139,140,141,142,143,144,145,146,148,149,150,151,152,153,154,155,156,157,158,159,160,163,166,168,169,171,172,173,175,176,177,178,180,181,182,183,],[37,38,41,44,45,48,49,52,55,56,59,62,37,41,44,48,52,55,59,62,-67,-72,-23,-24,-25,-81,-82,-83,-26,-84,-85,-86,-32,-33,-34,-35,-36,-87,-88,-89,-37,-38,-39,-43,-44,-50,-77,-79,-80,-56,-57,-58,-64,-65,-66,-71,-49,-51,-78,-55,]),'SIZE':([37,41,59,],[64,70,99,]),'PATH':([37,38,41,44,49,52,59,62,],[65,68,71,79,86,88,98,103,]),'FIT':([37,41,],[66,75,]),'UNIT':([37,41,],[67,73,]),'NAME':([41,44,52,56,],[72,80,90,96,]),'TYPE':([41,48,],[74,84,]),'DELETE':([41,],[76,]),'ADD':([41,],[77,]),'IDDISK':([45,48,52,55,],[81,83,89,93,]),'FS':([48,164,],[85,181,]),'RUTA':([52,],[91,]),'USER':([55,],[94,]),'PASS':([55,],[95,]),'CONT':([59,],[100,]),'R':([59,62,],[101,104,]),'IGUAL':([64,65,66,67,68,70,71,72,73,74,75,76,77,79,80,81,83,84,85,86,88,89,90,91,93,94,95,96,98,99,100,103,],[105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,]),'ENTERO':([105,110,117,120,121,123,126,129,131,134,],[137,148,158,161,162,164,167,170,172,176,]),'ROUTE':([106,109,111,118,124,125,128,133,135,136,],[138,147,149,159,165,166,169,175,177,178,]),'FIRSTFIT':([107,115,],[140,140,]),'BESTFIT':([107,115,],[141,141,]),'WORSTFIT':([107,115,],[142,142,]),'KILOBYTE':([108,113,],[144,144,]),'MEGABYTE':([108,113,],[145,145,]),'BYTES':([108,113,],[146,146,]),'ID':([112,119,127,130,131,132,161,162,167,170,],[150,160,168,171,173,174,179,180,182,183,]),'PRIMARY':([114,],[153,]),'EXTENDED':([114,],[154,]),'LOGIC':([114,],[155,]),'FULL':([116,122,],[157,163,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'list_commands':([0,],[2,]),'commands':([0,2,],[3,34,]),'command_mkdisk':([0,2,],[4,4,]),'command_rmdisk':([0,2,],[5,5,]),'command_fdisk':([0,2,],[6,6,]),'command_mount':([0,2,],[7,7,]),'command_unmount':([0,2,],[8,8,]),'command_mkfs':([0,2,],[9,9,]),'command_execute':([0,2,],[10,10,]),'command_rep':([0,2,],[11,11,]),'PartitionsMount':([0,2,],[12,12,]),'command_login':([0,2,],[13,13,]),'command_logout':([0,2,],[14,14,]),'command_mkgrp':([0,2,],[15,15,]),'command_mkfile':([0,2,],[16,16,]),'command_mkdir':([0,2,],[17,17,]),'command_pause':([0,2,],[18,18,]),'parameters_mkdisk':([19,36,],[35,63,]),'parameter_mkdisk':([19,36,],[36,36,]),'parameters_fdisk':([21,40,],[39,69,]),'parameter_fdisk':([21,40,],[40,40,]),'parameters_mount':([22,43,],[42,78,]),'parameter_mount':([22,43,],[43,43,]),'parameters_mkfs':([24,47,],[46,82,]),'parameter_mkfs':([24,47,],[47,47,]),'parameters_rep':([26,51,],[50,87,]),'parameter_rep':([26,51,],[51,51,]),'parameters_login':([28,54,],[53,92,]),'parameter_login':([28,54,],[54,54,]),'parameters_mkfile':([31,58,],[57,97,]),'parameter_mkfile':([31,58,],[58,58,]),'parameters_mkdir':([32,61,],[60,102,]),'parameter_mkdir':([32,61,],[61,61,]),'fit_options':([107,115,],[139,156,]),'unit_options':([108,113,],[143,151,]),'type_options':([114,],[152,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> list_commands','init',1,'p_init','parser_commands.py',25),
  ('list_commands -> list_commands commands','list_commands',2,'p_list_commands','parser_commands.py',31),
  ('list_commands -> commands','list_commands',1,'p_list_commands','parser_commands.py',32),
  ('commands -> command_mkdisk','commands',1,'p_commands','parser_commands.py',40),
  ('commands -> command_rmdisk','commands',1,'p_commands','parser_commands.py',41),
  ('commands -> command_fdisk','commands',1,'p_commands','parser_commands.py',42),
  ('commands -> command_mount','commands',1,'p_commands','parser_commands.py',43),
  ('commands -> command_unmount','commands',1,'p_commands','parser_commands.py',44),
  ('commands -> command_mkfs','commands',1,'p_commands','parser_commands.py',45),
  ('commands -> command_execute','commands',1,'p_commands','parser_commands.py',46),
  ('commands -> command_rep','commands',1,'p_commands','parser_commands.py',47),
  ('commands -> PartitionsMount','commands',1,'p_commands','parser_commands.py',48),
  ('commands -> command_login','commands',1,'p_commands','parser_commands.py',49),
  ('commands -> command_logout','commands',1,'p_commands','parser_commands.py',50),
  ('commands -> command_mkgrp','commands',1,'p_commands','parser_commands.py',51),
  ('commands -> command_mkfile','commands',1,'p_commands','parser_commands.py',52),
  ('commands -> command_mkdir','commands',1,'p_commands','parser_commands.py',53),
  ('commands -> command_pause','commands',1,'p_commands','parser_commands.py',54),
  ('PartitionsMount -> PM','PartitionsMount',1,'p_command_partitionsmount','parser_commands.py',60),
  ('command_mkdisk -> MKDISK parameters_mkdisk','command_mkdisk',2,'p_command_mkdisk','parser_commands.py',72),
  ('parameters_mkdisk -> parameter_mkdisk parameters_mkdisk','parameters_mkdisk',2,'p_parameters_mkdisk','parser_commands.py',85),
  ('parameters_mkdisk -> <empty>','parameters_mkdisk',0,'p_parameters_mkdisk','parser_commands.py',86),
  ('parameter_mkdisk -> GUION SIZE IGUAL ENTERO','parameter_mkdisk',4,'p_parameter_mkdisk','parser_commands.py',89),
  ('parameter_mkdisk -> GUION PATH IGUAL ROUTE','parameter_mkdisk',4,'p_parameter_mkdisk','parser_commands.py',90),
  ('parameter_mkdisk -> GUION FIT IGUAL fit_options','parameter_mkdisk',4,'p_parameter_mkdisk','parser_commands.py',91),
  ('parameter_mkdisk -> GUION UNIT IGUAL unit_options','parameter_mkdisk',4,'p_parameter_mkdisk','parser_commands.py',92),
  ('command_pause -> PAUSE','command_pause',1,'p_command_pause','parser_commands.py',110),
  ('command_rmdisk -> RMDISK GUION PATH IGUAL ROUTE','command_rmdisk',5,'p_command_rmdisk','parser_commands.py',114),
  ('command_fdisk -> FDISK parameters_fdisk','command_fdisk',2,'p_command_fdisk','parser_commands.py',126),
  ('parameters_fdisk -> parameter_fdisk parameters_fdisk','parameters_fdisk',2,'p_parameters_fdisk','parser_commands.py',141),
  ('parameters_fdisk -> <empty>','parameters_fdisk',0,'p_parameters_fdisk','parser_commands.py',142),
  ('parameter_fdisk -> GUION SIZE IGUAL ENTERO','parameter_fdisk',4,'p_parameter_fdisk','parser_commands.py',144),
  ('parameter_fdisk -> GUION PATH IGUAL ROUTE','parameter_fdisk',4,'p_parameter_fdisk','parser_commands.py',145),
  ('parameter_fdisk -> GUION NAME IGUAL ID','parameter_fdisk',4,'p_parameter_fdisk','parser_commands.py',146),
  ('parameter_fdisk -> GUION UNIT IGUAL unit_options','parameter_fdisk',4,'p_parameter_fdisk','parser_commands.py',147),
  ('parameter_fdisk -> GUION TYPE IGUAL type_options','parameter_fdisk',4,'p_parameter_fdisk','parser_commands.py',148),
  ('parameter_fdisk -> GUION FIT IGUAL fit_options','parameter_fdisk',4,'p_parameter_fdisk','parser_commands.py',149),
  ('parameter_fdisk -> GUION DELETE IGUAL FULL','parameter_fdisk',4,'p_parameter_fdisk','parser_commands.py',150),
  ('parameter_fdisk -> GUION ADD IGUAL ENTERO','parameter_fdisk',4,'p_parameter_fdisk','parser_commands.py',151),
  ('command_mount -> MOUNT parameters_mount','command_mount',2,'p_command_mount','parser_commands.py',172),
  ('parameters_mount -> parameter_mount parameters_mount','parameters_mount',2,'p_parameters_mount','parser_commands.py',184),
  ('parameters_mount -> <empty>','parameters_mount',0,'p_parameters_mount','parser_commands.py',185),
  ('parameter_mount -> GUION PATH IGUAL ROUTE','parameter_mount',4,'p_parameter_mount','parser_commands.py',188),
  ('parameter_mount -> GUION NAME IGUAL ID','parameter_mount',4,'p_parameter_mount','parser_commands.py',189),
  ('command_unmount -> UNMOUNT GUION IDDISK IGUAL ENTERO ID','command_unmount',6,'p_command_unmount','parser_commands.py',201),
  ('command_mkfs -> MKFS parameters_mkfs','command_mkfs',2,'p_command_mkfs','parser_commands.py',217),
  ('parameters_mkfs -> parameter_mkfs parameters_mkfs','parameters_mkfs',2,'p_parameters_mkfs','parser_commands.py',225),
  ('parameters_mkfs -> <empty>','parameters_mkfs',0,'p_parameters_mkfs','parser_commands.py',226),
  ('parameter_mkfs -> GUION IDDISK IGUAL ENTERO ID','parameter_mkfs',5,'p_parameter_mkfs','parser_commands.py',229),
  ('parameter_mkfs -> GUION TYPE IGUAL FULL','parameter_mkfs',4,'p_parameter_mkfs','parser_commands.py',230),
  ('parameter_mkfs -> GUION FS IGUAL ENTERO FS','parameter_mkfs',5,'p_parameter_mkfs','parser_commands.py',231),
  ('command_login -> LOGIN parameters_login','command_login',2,'p_command_login','parser_commands.py',247),
  ('parameters_login -> parameter_login parameters_login','parameters_login',2,'p_parameters_login','parser_commands.py',262),
  ('parameters_login -> <empty>','parameters_login',0,'p_parameters_login','parser_commands.py',263),
  ('parameter_login -> GUION IDDISK IGUAL ENTERO ID','parameter_login',5,'p_parameter_login','parser_commands.py',266),
  ('parameter_login -> GUION USER IGUAL ID','parameter_login',4,'p_parameter_login','parser_commands.py',267),
  ('parameter_login -> GUION PASS IGUAL ENTERO','parameter_login',4,'p_parameter_login','parser_commands.py',268),
  ('parameter_login -> GUION PASS IGUAL ID','parameter_login',4,'p_parameter_login','parser_commands.py',269),
  ('command_logout -> LOGOUT','command_logout',1,'p_command_logout','parser_commands.py',281),
  ('command_mkgrp -> MKGRP GUION NAME IGUAL ID','command_mkgrp',5,'p_command_mkgrp','parser_commands.py',287),
  ('command_mkfile -> MKFILE parameters_mkfile','command_mkfile',2,'p_command_mkfile','parser_commands.py',299),
  ('parameters_mkfile -> parameter_mkfile parameters_mkfile','parameters_mkfile',2,'p_parameters_mkfile','parser_commands.py',308),
  ('parameters_mkfile -> <empty>','parameters_mkfile',0,'p_parameters_mkfile','parser_commands.py',309),
  ('parameter_mkfile -> GUION PATH IGUAL ROUTE','parameter_mkfile',4,'p_parameter_mkfile','parser_commands.py',311),
  ('parameter_mkfile -> GUION SIZE IGUAL ENTERO','parameter_mkfile',4,'p_parameter_mkfile','parser_commands.py',312),
  ('parameter_mkfile -> GUION CONT IGUAL ROUTE','parameter_mkfile',4,'p_parameter_mkfile','parser_commands.py',313),
  ('parameter_mkfile -> GUION R','parameter_mkfile',2,'p_parameter_mkfile','parser_commands.py',314),
  ('command_mkdir -> MKDIR parameters_mkdir','command_mkdir',2,'p_command_mkdir','parser_commands.py',330),
  ('parameters_mkdir -> parameter_mkdir parameters_mkdir','parameters_mkdir',2,'p_parameters_mkdir','parser_commands.py',339),
  ('parameters_mkdir -> <empty>','parameters_mkdir',0,'p_parameters_mkdir','parser_commands.py',340),
  ('parameter_mkdir -> GUION PATH IGUAL ROUTE','parameter_mkdir',4,'p_parameter_mkdir','parser_commands.py',342),
  ('parameter_mkdir -> GUION R','parameter_mkdir',2,'p_parameter_mkdir','parser_commands.py',343),
  ('command_execute -> EXECUTE GUION PATH IGUAL ROUTE','command_execute',5,'p_command_execute','parser_commands.py',352),
  ('command_rep -> REP parameters_rep','command_rep',2,'p_command_rep','parser_commands.py',374),
  ('parameters_rep -> parameter_rep parameters_rep','parameters_rep',2,'p_parameters_rep','parser_commands.py',392),
  ('parameters_rep -> <empty>','parameters_rep',0,'p_parameters_rep','parser_commands.py',393),
  ('parameter_rep -> GUION PATH IGUAL ROUTE','parameter_rep',4,'p_parameter_rep','parser_commands.py',396),
  ('parameter_rep -> GUION IDDISK IGUAL ENTERO ID','parameter_rep',5,'p_parameter_rep','parser_commands.py',397),
  ('parameter_rep -> GUION NAME IGUAL ID','parameter_rep',4,'p_parameter_rep','parser_commands.py',398),
  ('parameter_rep -> GUION RUTA IGUAL ROUTE','parameter_rep',4,'p_parameter_rep','parser_commands.py',399),
  ('fit_options -> FIRSTFIT','fit_options',1,'p_fit_options','parser_commands.py',413),
  ('fit_options -> BESTFIT','fit_options',1,'p_fit_options','parser_commands.py',414),
  ('fit_options -> WORSTFIT','fit_options',1,'p_fit_options','parser_commands.py',415),
  ('unit_options -> KILOBYTE','unit_options',1,'p_unit_options','parser_commands.py',418),
  ('unit_options -> MEGABYTE','unit_options',1,'p_unit_options','parser_commands.py',419),
  ('unit_options -> BYTES','unit_options',1,'p_unit_options','parser_commands.py',420),
  ('type_options -> PRIMARY','type_options',1,'p_type_options','parser_commands.py',424),
  ('type_options -> EXTENDED','type_options',1,'p_type_options','parser_commands.py',425),
  ('type_options -> LOGIC','type_options',1,'p_type_options','parser_commands.py',426),
]
