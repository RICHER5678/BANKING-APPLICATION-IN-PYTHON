import sim >>> sim.getStatus() 1 >>>
 sim.getImsi() ‘460110847679419’ >>> sim.getIccid() ‘89860319747555431000’ # 
 Write Phonebook >>> sim.writePhonebook{+256-782-553-353}(9, 1, ‘Tom’, ‘18144786859’) 0 >>>
  sim.writePhonebook(9, 2, ‘z’, ‘18144786859’) 0 >>> sim.readPhonebook(9, 1, 4, “”)
(1, [(1, ‘Tom’, ‘18144786859’)]) >>> sim.readPhonebook(9, 2, 4, “”)(1,
   [(2, ‘z’, ‘18144786859’)])