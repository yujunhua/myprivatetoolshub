#include <winsock2.h>
#include <stdio.h>
#include <Ws2tcpip.h>
#pragma comment(lib, "ws2_32.lib")
void main()
{
	//��ʼ���׽���
	WORD wVersionRequested;
	WSADATA wsaData;
	wVersionRequested = MAKEWORD(2, 2);	
	WSAStartup(wVersionRequested, &wsaData);

	 //�����׽���
	SOCKET socSrv = socket(AF_INET, SOCK_STREAM, 0);

	//���׽���
	SOCKADDR_IN addrSrv;
	addrSrv.sin_addr.S_un.S_addr = htonl(INADDR_ANY);//ת��Unsigned long��Ϊ�����ֽ����ʽ
	addrSrv.sin_family = AF_INET;//ָ����ַ��
	addrSrv.sin_port = htons(6000);
	bind(socSrv, (SOCKADDR*)&addrSrv, sizeof(SOCKADDR));

	//�����׽���
	listen(socSrv, 5);//�ȴ����ӵ������г�����5
	SOCKADDR_IN addrClient;
	int len = sizeof(SOCKADDR);

	//��ʱ�����ڴ˷�������
	SOCKET sockConn = accept(socSrv, (SOCKADDR*)&addrClient, &len);


	char sendBuf[100] = { 0 };
	char recvBuf[100] = { 0 };//��ʼ��Ϊ0�������淢�͵�ʱ��strlen �Ͳ���Ҫ��1
	while (1)
	{
		//���ԭ������
		memset(sendBuf, 0, sizeof(sendBuf));
		gets_s(sendBuf);
		if (sendBuf[0] == '0')
			break;

		//char IPdotdec[10];
		//sprintf_s(sendBuf, "Welcome %s to Mars",
		//	inet_ntop(AF_INET, &addrClient.sin_addr, IPdotdec,10));//��ʽ�����

		//�÷��ص��׽��ֺͿͻ��˽���ͨ��
		send(sockConn, sendBuf, strlen(sendBuf), 0);

		//���ԭ������
		memset(recvBuf, 0, sizeof(recvBuf));
		//��������
		recv(sockConn, recvBuf, 100, 0);
		printf("%s\n", recvBuf);
		
	}
	closesocket(sockConn);
	printf("server close\n");
	WSACleanup();
}