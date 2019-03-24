import boto3

def get_face_comparison_confidence(sourceFile, targetFile, similarityThreshold=70):
    '''
      This function receives sourceFilePath and targetFilePath images. 
      Return the confidence level if it is above Similarity threshold (defult: 70)
    '''

    client=boto3.client('rekognition')

    imageSource=sourceFile
    imageTarget=open(targetFile,'rb')

    response=client.compare_faces(SimilarityThreshold=similarityThreshold,
                                  SourceImage={'Bytes': imageSource},
                                  TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + similarity + '% confidence')

    # imageSource.close()
    imageTarget.close()      
    return faceMatch['Similarity']   