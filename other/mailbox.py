def mailbox():
   result=[]
   mailbox=[x in xrange(99)]
   for y in yrange(5)
      for x in xrange(99)
         if(y==0)
            mailbox[x]=true
         if(y==1)
            if(x%2==0)
               mailbox[x]=false
         if(y==2)
            if (x%3==0) and (mailbox[x]==true)
                  mailbox[x]=false
            if (x%3==0) and (mailbox[x]==false)
                  mailbox[x]=true
         if(y==3)
            if (x%4==0) and (mailbox[x]==true)
                  mailbox[x]=false
            if (x%4==0) and (mailbox[x]==false)
                  mailbox[x]=true
         if(y==4)
            if (x%5==0) and (mailbox[x]==true)
                  mailbox[x]=false
            if (x%5==0) and (mailbox[x]==false)
                  mailbox[x]=true
   for z in xrange(100)
      if(mailbox[x]==true)
         result=result+[(x+1)]
   return result

print "The open mailboxes are...", mailbox()
