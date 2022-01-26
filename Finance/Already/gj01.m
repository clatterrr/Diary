data_path = 'D:\\whatsoever\\Finance\\';
data_name = 'AVAX';
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
ops_int5 = zeros(1,m);
eds_int5 = zeros(1,m);
his_int5 = zeros(1,m);
los_int5 = zeros(1,m);
ops_forward5 = zeros(1,m);
eds_forward5 = zeros(1,m);
his_forward5 = zeros(1,m);
los_forward5 = zeros(1,m);
for i = 2:m-1
    ops_diff1(i) = ops(i+1,1) - ops(i,1);
    eds_diff1(i) = eds(i+1) - eds(i);
    ops_diff2(i) = (ops(i+1) - ops(i-1))/2.0;
    eds_diff2(i) = (eds(i+1) - eds(i-1))/2.0;
end
for i = 3:m-2
    
end
for i = 5:m
    ops_forward5(i) = (2.5*ops(i) - 9.0*ops(i-1) + 12*ops(i-2) - 7*ops(i-3) + 1.5*ops(i-4));
    eds_forward5(i) = (2.5*eds(i) - 9.0*eds(i-1) + 12*eds(i-2) - 7*eds(i-3) + 1.5*eds(i-4));
    his_forward5(i) = (2.5*his(i) - 9.0*his(i-1) + 12*his(i-2) - 7*his(i-3) + 1.5*his(i-4));
    los_forward5(i) = (2.5*los(i) - 9.0*los(i-1) + 12*los(i-2) - 7*los(i-3) + 1.5*los(i-4));
    ops_int5(i) = (7 * ops(i-4) + 32 * ops(i-3) + 12 * ops(i-2) + 32 * ops(i-1) + 7 * ops(i)) * 0.01;
    eds_int5(i) = (7 * eds(i-4) + 32 * eds(i-3) + 12 * eds(i-2) + 32 * eds(i-1) + 7 * eds(i)) * 0.01;
    his_int5(i) = (7 * his(i-4) + 32 * his(i-3) + 12 * his(i-2) + 32 * his(i-1) + 7 * his(i)) * 0.01;
    los_int5(i) = (7 * los(i-4) + 32 * los(i-3) + 12 * los(i-2) + 32 * los(i-1) + 7 * los(i)) * 0.01;
    %ops_forward5(i) = (ops(i) - 4*ops(i-1) + 6*ops(i-2) - 4*ops(i-3) + ops(i-4));
end
oped_diff1 = ops_diff1 - eds_diff1;
oped_int2 = (ops_int2 - eds_int2)*20.0;
oped_forward5 = ops_forward5 - eds_forward5;
hilo_forward5 = ops_int5 - oped_forward5;
mix = his_int5 + ops_int5;

figure(6);
plot(x,eds,'b');
hold on;
descri = ' mix 5st int';
plot(x,mix * 0.5,'r');
plot(x,ops_int5,'g');
legend('price',descri);
set(gca, 'XTick', 1:5:m);
grid on;
xlim([0,100]);
title([data_name,descri]);
saveas(gcf,['D:\\whatsoever\\Finance\\',data_name,descri])
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
% figure(4);
% plot(x,ops);
% hold on;
% descri = ' open 5st int';
% plot(x,ops_int2);
% legend('price',descri);
% set(gca, 'XTick', 1:5:m);
% grid on;
% title([data_name,descri]);
% saveas(gcf,['D:\\whatsoever\\Finance\\',data_name,descri])
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
