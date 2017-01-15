%tmp and ind has most significant objects sorted



prompt={'Enter value for M: Ranked List',...
    'Enter the K value (Similar)',...
    'Enter the inputfile path',...
    'Enter the output directory to visualize',...
    };
dlg_title='Input for Task';
num_lines=1;
default={'10','2','C:\Users\naren\Desktop\Phase3\out_file_10_2.spc','C:\Users\naren\Desktop\SUBMIT P3\Task 3 Visual\'}; %need to change if someother laptpo
input=inputdlg(prompt,dlg_title,num_lines,default);
Kvalue=str2num(input{2});
inputfile=input{3};
outputfile=input{4};

Ma = str2num(input{1});
%Ma=10;
fileID=fopen(inputfile);
cellsFromFile = textscan(fileID,['{<%f,%f>,<%f,%f>,%f}']);
Rawdata = cell2mat(cellsFromFile); 
Predata = Rawdata(:,1);
startindex = 1;
 maxvcount = max(Rawdata(:,1));
 endindex=0;
 k=Kvalue;

            
            
for viter = 1:maxvcount
v_filtered = Rawdata(Rawdata(:, 1) == viter, :);
[row col] = size(v_filtered);
row = row/k;
endindex = endindex+row;
newmat(viter,1)  = startindex;
newmat(viter,2) = endindex;
startindex = endindex+1;

end


Matchdata = Rawdata(:,[3:4]);
[totrow totcol] = size(Rawdata);
T = zeros(totrow/k);
hashvalue = 1/k;


for i = 1:totrow
    colval = newmat(Rawdata(i, 3),1)+Rawdata(i, 4)-1;
    Matchdata(i,3) = colval;
    rowval = newmat(Rawdata(i, 1),1)+Rawdata(i, 2)-1;
    Rawdata(i,6) = rowval;
    Rawdata(i,7) = colval;
    T(rowval,colval) = Rawdata(i,5);
   
end

Totalframes = max(Rawdata(:,6));

 ODimension = [1:Totalframes];
 ODimension = transpose(ODimension);

T = transpose(T);

P(1:Totalframes,1) = 1/Totalframes;

alpha = 0.01;

%in matlab page :  r = (1-P)/n + P*(A'*(r./d) + s/n);  , s- node with 0
%edges, s = 0 in our case

firsthalf = zeros(Totalframes,1);
firsthalf(1:Totalframes,1) = ((1-alpha)/Totalframes);

Prod = firsthalf + alpha*(T*(P/k)); %gives the frame's significance
%Prod = (alpha*(T*P)) + ((1-alpha)*P);
value.OLD = ODimension;
 value.SCORE = Prod;
[tmp ind]=sort(value.SCORE,'descend'); %tmp and ind has proper values, printing this values


comptemp = zeros(Totalframes,1);

itercount = 2;
%test for convergence
while tmp(1,1) - comptemp(1,1) > power(1/10,itercount)
   itercount = itercount+1;
comptemp = tmp(1:Totalframes,1);
Prod = firsthalf + alpha*(T*(P/k)); %gives the frame's significance
%Prod = (alpha*(T*P)) + ((1-alpha)*P);
value.OLD = ODimension;
 value.SCORE = Prod;
[tmp ind]=sort(value.SCORE,'descend'); %tmp and ind has proper values, printing this values

difft = tmp-comptemp;

end



for s = 1:Totalframes
    for vdata = 1:maxvcount
        if ind(s,1) >= newmat(vdata,1) && ind(s,1)<= newmat(vdata,2)
            tmp(s,2) = vdata;
            tmp(s,3) = ind(s,1)-newmat(vdata,1)+1;
            
        end
    end
end


M = tmp([1:Ma],:);

