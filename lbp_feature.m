clc;
grayImage = imread('nikitaface.png'); % Read in image.
% Figure out where to divide it.
[rows, columns, numberOfColorChannels] = size(grayImage);
r3 = int32(rows/3);
c3 = int32(columns/3);
% Extract the 9 images.
face1 = grayImage(1:r3, 1:c3);
face2 = grayImage(1:r3, c3+1:2*c3);
face3 = grayImage(1:r3, 2*c3+1:columns);
face4 = grayImage(r3+1:2*r3, 1:c3);
face5 = grayImage(r3+1:2*r3, c3+1:2*c3);
face6 = grayImage(r3+1:2*r3, 2*c3+1:columns);
face7 = grayImage(2*r3+1:end, 1:c3);
face8 = grayImage(2*r3+1:end, c3+1:2*c3);
face9 = grayImage(2*r3+1:end, 2*c3+1:columns);

lbp_face = extractLBPFeatures(grayImage);
K = mean(lbp_face);
f = 3;
ak = 0.5*K;

grayImage = imread('nikitahand.png'); % Read in image.
% Figure out where to divide it.
[rows, columns, numberOfColorChannels] = size(grayImage);
r3 = int32(rows/3);
c3 = int32(columns/3);
% Extract the 9 images.
hand1 = grayImage(1:r3, 1:c3);
hand2 = grayImage(1:r3, c3+1:2*c3);
hand3 = grayImage(1:r3, 2*c3+1:columns);
hand4 = grayImage(r3+1:2*r3, 1:c3);
hand5 = grayImage(r3+1:2*r3, c3+1:2*c3);
hand6 = grayImage(r3+1:2*r3, 2*c3+1:columns);
hand7 = grayImage(2*r3+1:end, 1:c3);
hand8 = grayImage(2*r3+1:end, c3+1:2*c3);
hand9 = grayImage(2*r3+1:end, 2*c3+1:columns);

lbp_face1 = extractLBPFeatures(face1);
lbp_hand1 = extractLBPFeatures(hand1);

lbp_face2 = extractLBPFeatures(face2);
lbp_hand2 = extractLBPFeatures(hand2);

lbp_face3 = extractLBPFeatures(face3);
lbp_hand3 = extractLBPFeatures(hand3);

lbp_face4 = extractLBPFeatures(face4);
lbp_hand4 = extractLBPFeatures(hand4);

lbp_face5 = extractLBPFeatures(face5);
lbp_hand5 = extractLBPFeatures(hand5);

lbp_face6 = extractLBPFeatures(face6);
lbp_hand6 = extractLBPFeatures(hand6);

lbp_face7 = extractLBPFeatures(face7);
lbp_hand7 = extractLBPFeatures(hand7);

lbp_face8 = extractLBPFeatures(face8);
lbp_hand8 = extractLBPFeatures(hand8);

lbp_face9 = extractLBPFeatures(face9);
lbp_hand9 = extractLBPFeatures(hand9);

face_hand1 = (lbp_hand1 - lbp_face1).^2;
mf1 = meanfreq(face_hand1);

face_hand2 = (lbp_hand2 - lbp_face2).^2;
mf2 = meanfreq(face_hand2);

face_hand3 = (lbp_hand3 - lbp_face3).^2;
mf3 = meanfreq(face_hand3);

face_hand4 = (lbp_hand4 - lbp_face4).^2;
mf4 = meanfreq(face_hand4);

face_hand5 = (lbp_hand5 - lbp_face5).^2;
mf5 = meanfreq(face_hand5);

face_hand6 = (lbp_hand6 - lbp_face6).^2;
mf6 = meanfreq(face_hand6);

face_hand7 = (lbp_hand7 - lbp_face7).^2;
mf7 = meanfreq(face_hand7);

face_hand8 = (lbp_hand8 - lbp_face8).^2;
mf8 = meanfreq(face_hand8);

face_hand9 = (lbp_hand9 - lbp_face9).^2;
mf9 = meanfreq(face_hand9);

%figure
%bar([lbp_face]);

figure
bar([face_hand1],'grouped');
figure
bar([face_hand2],'grouped');
figure
bar([face_hand3],'grouped');
figure
bar([face_hand4],'grouped');
figure
bar([face_hand5],'grouped');
figure
bar([face_hand6],'grouped');
figure
bar([face_hand7],'grouped');
figure
bar([face_hand8],'grouped');
figure
bar([face_hand9],'grouped');
