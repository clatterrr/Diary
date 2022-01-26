data_path = 'D:\\whatsoever\\Finance\\';
data_name = 'ANT';
data_post = '.csv';
data = csvread([data_path,data_name,data_post]);
ops = data(:,2);
his = data(:,3);
los = data(:,4);
eds = data(:,5);
[m,n] = size(data);
x=linspace(1,m,m);
ops_diff1 = zeros(1,m);
eds_diff1 = zeros(1,m);
ops_diff2 = zeros(1,m);
eds_diff2 = zeros(1,m);
ops_int2 = zeros(1,m);
eds_int2 = zeros(1,m);
for i = 2:m-1
    ops_diff1(i) = ops(i+1,1) - ops(i,1);
    eds_diff1(i) = eds(i+1) - eds(i);
    ops_diff2(i) = (ops(i+1) - ops(i-1))/2.0;
    eds_diff2(i) = (eds(i+1) - eds(i-1))/2.0;
end
for i = 3:m-2
    ops_int2(i) = (7 * ops(i-2) + 32 * ops(i-1) + 12 * ops(i) + 32 * ops(i+1) + 7 * ops(i+2)) * 0.01;
    eds_int2(i) = (7 * eds(i-2) + 32 * eds(i-1) + 12 * eds(i) + 32 * eds(i+1) + 7 * eds(i+2)) * 0.01;
end
oped_diff1 = ops_diff1 - eds_diff1;
oped_int2 = (ops_int2 - eds_int2)*20.0;

% figure(1);
% plot(x,ops,'b');
% hold on;
% descri = ' open 2st d';
% plot(x,ops_diff1 + 10,'r');
% legend('price',descri);
% set(gca, 'XTick', 1:5:m);
% grid on;
% title([data_name,descri]);
% saveas(gcf,['D:\\whatsoever\\Finance\\',data_name,descri])
% 
% figure(2);
% plot(x,ops);
% hold on;
% descri = ' end 2st d';
% plot(x,eds_diff1 * 4);
% legend('price',descri);
% set(gca, 'XTick', 1:5:m);
% grid on;
% title([data_name,descri]);
% saveas(gcf,['D:\\whatsoever\\Finance\\',data_name,descri])
% 
% figure(3);
% plot(x,ops);
% hold on;
% descri = ' oped 2st d';
% plot(x,oped_diff1);
% legend('price',descri);
% set(gca, 'XTick', 1:5:m);
% grid on;
% title([data_name,descri]);
% saveas(gcf,['D:\\whatsoever\\Finance\\',data_name,descri])
% 
figure(4);
plot(x,ops);
hold on;
descri = ' open 5st int';
plot(x,ops_int2);
legend('price',descri);
set(gca, 'XTick', 1:5:m);
grid on;
title([data_name,descri]);
saveas(gcf,['D:\\whatsoever\\Finance\\',data_name,descri])
% 
% figure(5);
% plot(x,ops);
% hold on;
% descri = ' ed 5st int';
% plot(x,eds_int2);
% legend('price',descri);
% set(gca, 'XTick', 1:5:m);
% grid on;
% title([data_name,descri]);
% saveas(gcf,['D:\\whatsoever\\Finance\\',data_name,descri])
% 
% figure(6);
% plot(x,ops);
% hold on;
% descri = ' oped 5st int';
% plot(x,oped_int2);
% legend('price',descri);
% set(gca, 'XTick', 1:5:m);
% grid on;
% title([data_name,descri]);
% saveas(gcf,['D:\\whatsoever\\Finance\\',data_name,descri])