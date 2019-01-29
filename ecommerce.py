def linearregression():
	import graphlab
	sales=graphlab.SFrame('C:\Users\DEEP\machine learning\course2\home_data.gl')
	train_data,test_data=sales.random_split(.8,seed=0)
	my_features=['bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'yr_built', 'zipcode']
	model=graphlab.linear_regression.create(train_data,target='price',features=my_features,validation_set=None)
        print """\n\n							1. CHOOSE HOUSE FROM DATASET\n
                      						(use house id)
                             
									OR
                 
							2. ENTER ATTRIBUTES OF HOUSE MANUALLY\n
        			[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, yr_built, zipcode]\n\n"""
	a=raw_input()
	if a=='1':
		print "\n\nENTER HOUSE ID"
		id=raw_input()
		house=sales[sales['id']==id]
		print "\n\nATTRIBUTES OF THE SELECTED HOUSE"
		print house
	elif a=='2':
                b=[raw_input() for i in range(10)]
		b=[int(i) for i in b]
	        house={'bedrooms':b[0],'bathrooms':b[1],'sqft_living':b[2],'sqft_lot':b[3],'floors':b[4],'waterfront':b[5],'view':b[6],'condition':b[7],'yr_built':b[8],'zipcode':b[9]}	 
	
	print "\n\nPREDICTED HOUSE PRICE FOR SELECTED HOUSE....\n"
	print model.predict(house)
	    

def sentiment():
	import graphlab
	products=graphlab.SFrame('C:\Users\DEEP\machine learning\course3\data.gl')
	products=products[products['rating']!=3]
	products['word_count']=graphlab.text_analytics.count_words(products['review'])
	products['sentiment']=products['rating']>=4
	train_data,test_data=products.random_split(.8,seed=0)
	sentiment_model=graphlab.logistic_classifier.create(train_data,target='sentiment',features=['word_count'],validation_set=test_data)
	print """\n\n\t\t\t\t\t\t\t1. ENTER YOUR REVIEW TO CHECK SENTIMENT
	\n\t\t\t\t\t\t\t\tOR 
	\n\t\t\t\t\t\t\t2. UPDATE SENTIMENT IN DATASET"""
	n=raw_input()
	if n=='1':
		print "ENTER REVIEW"
		n=raw_input()
		n=graphlab.SFrame({'review':[n]})
		n['word_count']=graphlab.text_analytics.count_words(n['review'])
		s=sentiment_model.predict(n,output_type='probability')
 		if s[0]>0.5:
			print "\n\n..POSITIVE REVIEW..\n"
			print "PROBABILITY"
			print s
		else:
			print "\n\n..NEGATIVE REVIEW..\n"
			print "PROBABILITY"
			print s
	elif n=='2':
		products['predicted_sentiment']=sentiment_model.predict(products,output_type='probability')
		print products
	

c='yes'
while c!='no':
	print """\n\n\n\n                                  				...LET THE MACHINE
                                  				   DO YOUR BUSINESS...
						
							
						      ..// THE AUTOMATIC E-COMMERCE EXPERIENCE //..
				
							
							 1.PRICE YOUR PRODUCT
						
							 2.ANALYSE THE SENTIMENT OF REVIEW

                                                   
						      PLEASE CHOOSE FROM THE CATEGORIES ABOVE"""
	
	n=raw_input()
        if n=='1':
		linearregression()
	elif n=='2':
		sentiment()

	print """\n\n\t\t\t\t\t\tREDIRECT TO THE MAIN MENU
	\t\t\t\t\tYES
	\t\t\t\t\tNO\n\n"""
        c=raw_input()


	
       